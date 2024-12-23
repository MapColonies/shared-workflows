#!/usr/bin/env python 

import argparse
import json
import os
import ruamel.yaml


DEPLOYMENT_F_NAME = "deployment.json"
HELM_CHART_F_NAME = "Chart.yaml"


def build_deployment_path(charts_root, scope):
    return os.path.join(charts_root, scope, DEPLOYMENT_F_NAME)


def check_dependency_in_chart(file_path, dependency_name):
    """
    Function to check if a dependency exists in the chart
    """
    with open(file_path, 'r') as file:
        yaml = ruamel.yaml.YAML()
        chart_data = yaml.load(file)

    # Check if dependencies exists in the chart data
    if 'dependencies' in chart_data:
        # Loop through the dependencies to check for the given name
        for dependency in chart_data['dependencies']:
            if dependency.get('name') == dependency_name:
                print(f"Found dependency {dependency_name}")
                return True
    return False


def get_charts_candidates(file_path, service_name, charts_root_path):
    """
    Function to load and process deployment object.
    """
    chart_candidates = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Example processing logic: print all objects
        for obj in data:
            print(f"Processing object: {obj}")
            chart_location = obj.get('chartLocation')
            if chart_location:
                if check_dependency_in_chart(os.path.join(charts_root_path, chart_location, HELM_CHART_F_NAME), service_name):
                    chart_candidates.append(obj)
                print(f"Chart location is {chart_location}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file_path}.")
    return chart_candidates

def get_versions(service_version):
    """
    Function which prepares the helm and docker version
    """
    docker_version = service_version
    helm_version = service_version.removeprefix("v")
    return docker_version, helm_version


def update_helm_dependency_version(chart_path, dependency_name, new_version):
    found_dependency = False
    # Open and read the chart.yaml file
    with open(chart_path, 'r') as file:
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        chart_data = yaml.load(file)

    for dependency in chart_data['dependencies']:
        if dependency.get('name') == dependency_name:
            # Update the version of the dependency
            dependency['version'] = new_version
            found_dependency = True
            break

    # Save the updated data back to the chart.yaml file
    if found_dependency:
        with open(chart_path, 'w') as file:
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(chart_data, file)
        print(f"Updated '{dependency_name}' version to {new_version} in Chart.yaml({chart_path}).")


def update_docker_version(values_file, service_name, new_version):
    found_service_image_tag = False
    # Open and read the chart.yaml file
    with open(values_file, 'r') as file:
        # chart_data = yaml.safe_load(file)
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        chart_data = yaml.load(file)
    if service_name in chart_data:
        if 'image' in chart_data[service_name]:
            if 'tag' in chart_data[service_name]['image']:
                chart_data[service_name]['image']['tag'] = new_version
                found_service_image_tag = True

    # Save the updated data back to the chart.yaml file
    if found_service_image_tag:
        with open(values_file, 'w') as file:
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(chart_data, file)
        print(f"Updated '{service_name}' docker version to {new_version} in values file({values_file}).")


def find_replace_chart_versions(service_name, charts_root_path, service_version, scope):
    """
    Function which finds the charts which should be updated
    and updates all the chart references versions
    and the image versions
    """
    deployment_full_path = build_deployment_path(charts_root_path, scope)
    print(f"deployment_full_path={deployment_full_path}")
    charts_to_process = get_charts_candidates(deployment_full_path, service_name, charts_root_path)
    docker_version, helm_version = get_versions(service_version)
    print(f"docker_version={docker_version}")
    print(f"helm_version={helm_version}")
    for obj in charts_to_process:
        chart_location = obj.get('chartLocation')
        if chart_location:
            chart_yaml_path = os.path.join(charts_root_path, chart_location, HELM_CHART_F_NAME)
            print(f"chart_yaml_path={chart_yaml_path}")
            update_helm_dependency_version(chart_yaml_path, service_name, helm_version)
        values_files = obj.get('valuesFile')
        if values_files:
            for v_file in values_files:
                v_file_yaml_path = os.path.join(charts_root_path, v_file)
                update_docker_version(v_file_yaml_path, service_name, docker_version)


def parse_arguments():
    """
    Function to handle argument parsing.
    """
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Image updater")
    parser.add_argument('--charts-root-path', dest='charts_root_path', type=str,
                        help='The path to the helm charts root repo', required=True)
    parser.add_argument('--scope', dest='scope', type=str,
                        help='The scope / team name of the chart', required=True)
    parser.add_argument('--service-name', dest='service_name', type=str,
                        help='The service name / repository',required=True)
    parser.add_argument('--service-version', dest='service_version', type=str,
                        help='The service version',required=True)

    
    # Parse arguments from the command line
    args = parser.parse_args()
    print(f"charts_root_path is {args.charts_root_path}")
    print(f"scope is {args.scope}")
    print(f"service name is {args.service_name}")
    print(f"service version is {args.service_version}")
    return args   


def main():
    """
    Main function that ties everything together.
    """
    # Parse the arguments
    args = parse_arguments()
    find_replace_chart_versions(args.service_name, args.charts_root_path, args.service_version, args.scope)

if __name__ == "__main__":
    main()
