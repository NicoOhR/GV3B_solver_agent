from pybuilder.core import use_plugin, init, task
import requests

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

default_task = ["get_protobuf_service_def", "publish"]


@init
def set_properties(project):
    project.build_depends_on("requests")
    project.build_depends_on("grpcio")
    project.build_depends_on("grpcio-tools")
    project.build_depends_on("protobuf")


@task
def get_protobuf_service_def(project):
    protobuf_url = "https://github.com/NicoOhR/GV3B_simulation/blob/main/proto/simulation.protobuf_url"
    response = requests.get(protobuf_url)
    if response.status_code == 200:
        with open("simulation.proto", "wb") as file:
            file.write(response.content)
            print("Successfuly got latest protobuf")
    else:
        print("Failed to get protobuf")
