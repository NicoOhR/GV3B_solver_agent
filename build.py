from pybuilder.core import use_plugin, init, task
import requests
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

default_task = ["publish"]


@init
def set_properties(project):
    project.build_depends_on("requests")
    project.build_depends_on("grpcio")
    project.build_depends_on("grpcio-tools")
    project.build_depends_on("protobuf")
    get_protobuf_service_def(project)


def get_protobuf_service_def(project):
    protobuf_url = "https://raw.githubusercontent.com/NicoOhR/GV3B_simulation/refs/heads/main/proto/simulation.proto"
    response = requests.get(protobuf_url)
    if response.status_code == 200:
        proto_file = os.path.join(project.basedir, "proto/simulation.proto")
        proto_dir = os.path.join(project.basedir, "proto/")
        os.makedirs(proto_dir, exist_ok=True)
        with open(proto_file, "wb") as file:
            file.write(response.content)
            print("[Builder] Successfuly got latest protobuf")
    else:
        print("[Builder] Failed to get protobuf")
        print(response.status_code)
