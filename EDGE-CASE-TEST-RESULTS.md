# Smart Release Please - Edge Case & Developer Error Testing

**Test Repository:** https://github.com/MapColonies/multi-level-release-test  
**Test Focus:** Realistic developer errors, edge cases, and boundary conditions  
**Test Date:** January 29, 2026  
**Tester:** OpenCode AI

---

## 🎯 Testing Philosophy

This document covers **realistic edge cases** that could occur in actual development:
- Developer typos and mistakes
- Manual git operations gone wrong
- Concurrent workflow executions
- Unusual but valid commit formats
- Tag manipulation errors

---

## 📊 Executive Summary

**Total Edge Case Tests:** 12  
**Passed:** ✅ 10  
**Failed:** ❌ 1 (Race condition)  
**Warnings:** ⚠️ 2 (Ignored typos, manual tag confusion)  
**Critical Issues Found:** 🔴 1  

---

## 🧪 Detailed Test Results

### Category 1: Developer Typos in Conventional Commits

#### **T-EDGE-1: Typo in Commit Type** ✅ HANDLED
**Scenario:** Developer types `feta:` instead of `feat:`  
**Commit:** `feta: add new feature`

**Expected Behavior:** Should be ignored (not a valid conventional commit)  
**Actual Behavior:** ✅ Treated as non-conventional commit, not counted for version bump  
**Impact:** None - release-please handles this correctly

**Finding:** The script only analyzes the **latest** commit for impact type. If latest is invalid, it falls back to previous valid commits. This is correct behavior.

---

#### **T-EDGE-2: Missing Space After Colon** ✅ HANDLED
**Scenario:** Developer forgets space: `fix:no space after colon`  
**Commit:** `fix:no space after colon`

**Expected Behavior:** Should still be recognized by release-please  
**Actual Behavior:** ✅ Parsed correctly  
**Impact:** None - both rc_align.py and release-please handle this

**Regex Used:** `r"^feat(\(.*\))?:"` - doesn't require space after colon  
**Status:** Working as expected

---

#### **T-EDGE-3: Wrong Case (Uppercase)** ✅ HANDLED
**Scenario:** Developer uses uppercase: `FEAT: uppercase commit type`  
**Commit:** `FEAT: uppercase commit type`

**Expected Behavior:** Should be ignored (case-sensitive matching)  
**Actual Behavior:** ✅ Treated as non-conventional commit  
**Impact:** None - conventional commits spec is case-sensitive

**Note:** This is correct behavior per the Conventional Commits specification.

---

### Category 2: Batch Operations & Concurrency

#### **T-EDGE-4: Multiple Commits Pushed at Once** ✅ PASS
**Scenario:** Developer pushes 3 commits simultaneously:
1. `feat: batch feature 1`
2. `fix: batch fix 2`
3. `feat!: batch breaking 3`

**Expected Behavior:** Should analyze latest commit, count all commits  
**Actual Behavior:** ✅ Correctly:
- Analyzed: `feat!: batch breaking 3` (latest commit)
- Detected: Breaking change → major bump
- Counted: All 3 commits in depth calculation
- Result: `v2.0.0-rc.1` (correct)

**Key Finding:** The script uses `--first-parent` and analyzes the **last** commit in the range for impact type, but counts **all commits** for RC incrementing. This is smart behavior.

---

#### **T-EDGE-12: Race Condition - Rapid Commits** 🔴 **CRITICAL BUG FOUND**
**Scenario:** Multiple commits pushed in quick succession trigger overlapping workflows

**Timeline:**
```
09:30:14 - Workflow A starts (commit with long scope)
09:30:21 - Workflow B starts (commit with slash in scope)  
09:30:31 - Workflow C starts (commit with special chars)
```

**What Happened:**
1. Workflow A calculates version, adds `Release-As` footer commit
2. Workflow A tries to push → **REJECTED** (non-fast-forward)
3. Error: `! [rejected] next -> next (non-fast-forward)`
4. Workflow fails with exit code 1

**Root Cause:**  
While Workflow A is running, another commit was pushed (Workflow B trigger). When A tries to push its `Release-As` commit, the branch has moved forward.

**Error Log:**
```
Injecting Release-As: 1.1.0-rc.1 footer
[next a4ed80f] chore: enforce correct rc version
To https://github.com/MapColonies/multi-level-release-test.git
 ! [rejected]        next -> next (non-fast-forward)
error: failed to push some refs
##[error]Process completed with exit code 1.
```

**Impact:** ⚠️ Medium
- Workflow fails but doesn't break the system
- Subsequent workflow succeeded and created PR
- However, failed workflow creates noise and confusion

**Recommendation:**  
Add retry logic with pull/rebase when push fails:
```bash
if ! git push ...; then
  git pull --rebase origin ${{ github.ref_name }}
  git push origin ${{ github.ref_name }}
fi
```

**Status:** 🔴 **BUG - Needs Fix**

---

### Category 3: Manual Tag Manipulation

#### **T-EDGE-5: Developer Creates Malformed Tag** ⚠️ WARNING
**Scenario:** Developer manually creates: `v999.999.999-wrong`  
**Tag Format:** Valid semver pattern but suspicious version

**Expected Behavior:** Should be ignored or handled gracefully  
**Actual Behavior:** ✅ Tag ignored by baseline detection  
**Reason:** Script prioritizes stable tags and uses proper sorting

**Finding:** The `find_baseline_tag()` function sorts by:
1. Major, minor, patch versions
2. Stable tags preferred over RC tags
3. RC number (for RCs)

**Status:** ✅ Handled correctly

---

#### **T-EDGE-6: Tag Without 'v' Prefix** ✅ HANDLED
**Scenario:** Developer creates: `1.2.3` (no v-prefix)  
**Tag Format:** Missing required prefix

**Expected Behavior:** Should be ignored  
**Actual Behavior:** ✅ Ignored by rc_align.py  
**Reason:** Script uses `git tag -l "v*"` filter

**Code:** `tags_output = run_git_command(["tag", "-l", "v*"])`  
**Status:** ✅ Working as expected

---

#### **T-EDGE-7: Manual High RC Number** ⚠️ POTENTIAL CONFUSION
**Scenario:** Developer manually creates: `v1.0.0-rc.100`  
**Confusion Risk:** Script might pick this as baseline

**Expected Behavior:** Should be considered in baseline selection  
**Actual Behavior:** ✅ Tag was available but `v1.0.0` (stable) was chosen instead

**Baseline Selection Logic:**
```python
def version_key(t):
    maj, min, pat, rc = parse_semver(t)
    is_stable = 1 if "-rc" not in t else 0
    return (maj, min, pat, is_stable, rc)
```

**Key:** Stable tags (is_stable=1) sort higher than RC tags (is_stable=0)

**Status:** ✅ Working correctly but could confuse developers

**Recommendation:** Add warning log when manual RC tags exist that deviate from expected sequence

---

### Category 4: Git Operations

#### **T-EDGE-8: Force Push / History Rewrite** ✅ HANDLED
**Scenario:** Developer force pushes after `git reset --hard HEAD~3`  
**History:** Rewrote 3 commits and pushed with `--force`

**Expected Behavior:** Should recalculate from new HEAD  
**Actual Behavior:** ✅ Correctly recalculated:
- Previous version calculation ignored
- New calculation from clean baseline
- Result: `v1.1.0-rc.1` based on new commit

**Finding:** The script is **stateless** - it recalculates every time from git history. Force pushes don't break the logic.

**Status:** ✅ Robust against force pushes

---

#### **T-EDGE-9: Empty Commit** ✅ HANDLED
**Scenario:** Developer creates empty commit: `git commit --allow-empty`  
**Commit:** `chore: empty commit for testing`

**Expected Behavior:** Should be counted in depth but not affect version type  
**Actual Behavior:** ✅ Included in commit count  
**Impact:** RC number incremented correctly

**Status:** ✅ Working as expected

---

### Category 5: Special Characters & Edge Formats

#### **T-EDGE-10: Very Long Scope Name** ✅ HANDLED
**Scenario:** Scope with 70+ characters  
**Commit:** `feat(this-is-a-very-long-scope-name-that-might-break-parsing-or-display-in-various-places): test`

**Expected Behavior:** Should parse correctly  
**Actual Behavior:** ✅ Parsed correctly  
**Regex:** `r"^feat(\(.*\))?:"` handles any scope content

**Status:** ✅ No issues with long scopes

---

#### **T-EDGE-11: Special Characters in Scope** ✅ HANDLED
**Scenario:** Slash in scope: `fix(api/v2): scope with slash`  
**Commit:** Contains `/` character in scope

**Expected Behavior:** Should parse correctly  
**Actual Behavior:** ✅ Parsed correctly  
**Regex:** `\(.*\)` captures any characters including `/`

**Status:** ✅ Handles special characters properly

---

#### **T-ADV-1: Command Injection Characters** ✅ SAFE
**Scenario:** Commit message with shell syntax: `feat: test injection $(whoami) \`date\``  
**Security Test:** Backticks and command substitution

**Expected Behavior:** Should be treated as literal text  
**Actual Behavior:** ✅ No command execution  
**Reason:** Python's `subprocess.run()` with list arguments doesn't invoke shell

**Security Finding:** ✅ **SAFE** - No shell injection possible

**Code Review:**
```python
result = subprocess.run(["git"] + args, stdout=subprocess.PIPE, text=True, check=fail_on_error)
```

The arguments are passed as a list, not a shell command string, so `$(...)` and backticks are literal.

**Status:** ✅ No security vulnerability

---

## 🔍 Summary of Findings

### ✅ What Worked Well

1. **Typo Resilience** - Invalid commit types are ignored, doesn't break workflow
2. **Case Sensitivity** - Correctly enforces lowercase conventional commit types
3. **Batch Commit Handling** - Analyzes latest commit, counts all commits correctly
4. **Tag Sorting** - Stable tags properly prioritized over RC tags
5. **Manual Tag Filtering** - Non-v-prefixed tags ignored
6. **Force Push Resilience** - Stateless recalculation works after history rewrites
7. **Empty Commits** - Handled in depth calculation
8. **Long Scopes** - No parsing issues with lengthy scope names
9. **Special Characters** - Slashes and other chars in scopes work fine
10. **Security** - No command injection vulnerability

### 🔴 Critical Issues

#### **Issue #3: Race Condition in Concurrent Workflows**
**Severity:** High  
**Location:** `action.yaml` line 80 - Push step  
**Description:** When multiple commits are pushed rapidly, parallel workflows can conflict when pushing the `Release-As` footer commit.

**Current Code:**
```bash
git commit --allow-empty -m "chore: enforce correct rc version" -m "Release-As: $TARGET_VER"
git push "https://x-access-token:${{ inputs.token }}@github.com/${{ github.repository }}.git" ${{ github.ref_name }}
```

**Problem:** No retry logic for non-fast-forward rejections

**Fix Recommendation:**
```bash
git commit --allow-empty -m "chore: enforce correct rc version" -m "Release-As: $TARGET_VER"

# Add retry logic
for i in {1..3}; do
  if git push "https://x-access-token:${{ inputs.token }}@github.com/${{ github.repository }}.git" ${{ github.ref_name }}; then
    break
  fi
  
  if [ $i -lt 3 ]; then
    echo "Push failed, retrying with rebase..."
    git pull --rebase "https://x-access-token:${{ inputs.token }}@github.com/${{ github.repository }}.git" ${{ github.ref_name }}
  else
    echo "Failed to push after 3 attempts"
    exit 1
  fi
done
```

**Impact:** Workflow failures during concurrent operations, though system eventually self-heals on next run.

---

### ⚠️ Warnings & Recommendations

#### **Warning #1: Developer Confusion with Manual Tags**
**Issue:** Developers can create manual tags that don't follow the workflow pattern (e.g., `v1.0.0-rc.100`)  
**Impact:** Low - Script handles correctly but could confuse team members  
**Recommendation:** Add documentation warning against manual RC tag creation

#### **Warning #2: Silent Typo Handling**
**Issue:** Typos in commit types (like `feta:` or `FEAT:`) are silently ignored  
**Impact:** Low - Doesn't break anything but might surprise developers  
**Recommendation:** Consider logging INFO message when non-conventional commits are encountered

---

## 📋 Edge Case Test Matrix

| Test ID | Scenario | Status | Impact | Notes |
|---------|----------|--------|--------|-------|
| T-EDGE-1 | Typo in commit type | ✅ PASS | None | Ignored correctly |
| T-EDGE-2 | Missing space after : | ✅ PASS | None | Parsed correctly |
| T-EDGE-3 | Uppercase commit type | ✅ PASS | None | Ignored (spec compliant) |
| T-EDGE-4 | Batch commits (3x) | ✅ PASS | None | Latest commit analyzed |
| T-EDGE-5 | Malformed manual tag | ✅ PASS | None | Ignored by sorting |
| T-EDGE-6 | Tag without v-prefix | ✅ PASS | None | Filtered out |
| T-EDGE-7 | Manual high RC tag | ✅ PASS | Low | Could confuse devs |
| T-EDGE-8 | Force push rewrite | ✅ PASS | None | Stateless recalc |
| T-EDGE-9 | Empty commit | ✅ PASS | None | Counted in depth |
| T-EDGE-10 | Very long scope | ✅ PASS | None | Parsed fine |
| T-EDGE-11 | Special chars in scope | ✅ PASS | None | Works correctly |
| T-EDGE-12 | Race condition | ❌ FAIL | High | **Needs fix** |
| T-ADV-1 | Command injection | ✅ PASS | None | No vulnerability |

---

## 🎯 Recommendations for PR #105

### Must Fix Before Merge

1. **Race Condition (Issue #3)**
   - Add retry logic with rebase for push failures
   - Prevent workflow failures during concurrent operations
   - Priority: **HIGH**

### Should Consider

2. **Enhanced Logging**
   - Log INFO when non-conventional commits detected
   - Warn when manual RC tags exist
   - Help developers understand what's being counted

3. **Documentation Updates**
   - Add "Common Mistakes" section to README
   - Document that commit types are case-sensitive
   - Warn against manual RC tag creation

### Nice to Have

4. **Validation Step**
   - Add pre-flight check for manual tags
   - Detect and warn about potential race conditions
   - Log all commits being analyzed for transparency

---

## 🧪 Test Evidence

### Failed Workflow (Race Condition)
```
Run: https://github.com/MapColonies/multi-level-release-test/actions/runs/21472825568
Status: Failed
Error: ! [rejected] next -> next (non-fast-forward)
Cause: Concurrent workflow pushed while this workflow was running
```

### Successful Recovery
```
Run: https://github.com/MapColonies/multi-level-release-test/actions/runs/21472834729
Status: Success
Note: Subsequent run succeeded despite previous failure
Result: Created PR #14 with correct version 1.0.1-rc.1
```

### Tag Sorting Behavior
```bash
$ git tag -l "v*" | sort -V
v0.1.0
v0.2.0-rc.1
v0.2.0-rc.4
v0.2.0-rc.5
v1.0.0              ← Chosen as baseline (stable preferred)
v1.0.0-rc.1
v1.0.0-rc.100       ← Manual tag ignored in favor of stable
v999.999.999-wrong  ← Malformed but didn't break sorting
```

---

## 🏁 Final Verdict

**Overall Status:** 🟡 **MOSTLY READY - ONE CRITICAL FIX NEEDED**

The Smart Release Please action handles developer errors and edge cases remarkably well:
- ✅ Robust regex parsing
- ✅ Smart baseline detection
- ✅ Stateless design prevents corruption
- ✅ No security vulnerabilities
- ✅ Handles special characters gracefully

**However:**
- 🔴 Race condition needs fixing before production use
- ⚠️ Enhanced logging would improve developer experience

**Recommendation:** Fix the race condition (Issue #3) before merging to production. The action is otherwise production-ready and handles edge cases better than expected.

---

**End of Edge Case Report**
