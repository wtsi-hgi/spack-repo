# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyRay(PythonPackage):
    """Ray provides a simple, universal API for building distributed applications."""

    homepage = "https://github.com/ray-project/ray"
    url = "https://github.com/ray-project/ray/archive/refs/tags/ray-2.33.0.tar.gz"

    version("2.42.0", sha256="f3cc6abb632f38f8680c9456e57ab320d32ecbef2164b74ff5ee0f0c7adeb57e")

    variant("default", default=False, description="Install default extras", when="@2")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("bazel@6.5", when="@2.42.0", type="build")
    depends_on("npm", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@3:", type="build")
    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-click@7:8.0.4", type=("build", "run"))
    depends_on("py-filelock", type=("build", "run"))
    depends_on("py-grpcio@1.32:1.43.0", when="^python@:3.9", type=("build", "run"))
    depends_on("py-grpcio@1.42:1.43.0", when="^python@3.10:", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-msgpack@1", type=("build", "run"))
    depends_on("py-numpy@1.16:", when="^python@:3.8", type=("build", "run"))
    depends_on("py-numpy@1.19.3:", when="^python@3.9:", type=("build", "run"))
    depends_on("py-protobuf@3.15.3:3", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-frozenlist", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-typing-extensions", when="^python@:3.7", type=("build", "run"))
    depends_on("py-virtualenv", type=("build", "run"))
    depends_on("boost@1.74:", type=("build", "run", "link"))

    with when("+default"):
        depends_on("py-aiohttp@3.7:", type=("build", "run"))
        depends_on("py-aiohttp-cors", type=("build", "run"))
        depends_on("py-colorful", type=("build", "run"))
        depends_on("py-py-spy@0.2:", type=("build", "run"))
        depends_on("py-gpustat@1:", type=("build", "run"))
        depends_on("py-opencensus", type=("build", "run"))
        depends_on("py-pydantic", type=("build", "run"))
        depends_on("py-prometheus-client@0.7.1:0.13", type=("build", "run"))
        depends_on("py-smart-open", type=("build", "run"))

    build_directory = "python"

    def patch(self):
        filter_file(
            'bazel_flags = ["--verbose_failures"]',
            f'bazel_flags = ["--verbose_failures", "--jobs={make_jobs}"]',
            join_path("python", "setup.py"),
            string=True,
        )

    def setup_build_environment(self, env):
        env.set("SKIP_THIRDPARTY_INSTALL", "1")
        env.set("NODE_OPTIONS", "--openssl-legacy-provider")

    # Compile the dashboard npm modules included in the project
    @run_before("install")
    def build_dashboard(self):
        with working_dir(join_path("python", "ray", "dashboard", "client")):
            npm = which("npm")
            npm("ci")
            npm("run", "build")
