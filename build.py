from pybuilder.core import use_plugin, init, task
import subprocess
import requests
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

default_task = ["get_protobuf_service_def", "build_proto_buf", "publish"]


@init
def set_properties(project):
    project.build_depends_on("requests")
    project.build_depends_on("grpcio")
    project.build_depends_on("grpcio-tools")
    project.build_depends_on("protobuf")


@task
def get_protobuf_service_def(project):
    protobuf_url = "https://raw.githubusercontent.com/NicoOhR/GV3B_simulation/refs/heads/main/proto/simulation.proto"
    response = requests.get(protobuf_url)
    if response.status_code == 200:
        proto_dir = os.path.join(
            project.get_property("dir_source_main_python"), "proto"
        )
        proto_file = os.path.join(proto_dir, "simulation.proto")
        project.set_property("proto_dir", proto_dir)
        project.set_property("proto_file", proto_file)
        os.makedirs(proto_dir, exist_ok=True)
        with open(proto_file, "wb") as file:
            file.write(response.content)
            print("[Builder] Successfuly got latest protobuf")
    else:
        print("[Builder] Failed to get protobuf")
        print(response.status_code)


@task
def build_proto_buf(project):
    proto_file = project.get_property("proto_file")
    proto_dir = project.get_property("proto_dir")
    module_file = os.path.join(proto_dir, "__init__.py")
    command = [
        "python3",
        "-m",
        "grpc_tools.protoc",
        "-I",
        proto_dir,
        f"--python_out={proto_dir}",
        f"--grpc_python_out={proto_dir}",
        proto_file,
    ]

    try:
        result = subprocess.run(command, text=True, check=True)
        print("[Builder] Protobuf compilation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[Builder] Protobuf compilation failed with error code {e.returncode}")
    except FileNotFoundError:
        print(
            "[Builder] Python3 or grpc_tools not found. Ensure they are installed and available in PATH."
        )
    except Exception as e:
        print(f"[Builder] An unexpected error occurred: {e}")

    with open(module_file, "a"):
        pass
