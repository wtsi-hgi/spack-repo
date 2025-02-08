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
    # version("2.41.0", sha256="6618b48042047d16549a70d563ba093c8d25a5b9f3f0196e192a5add6e297a5a")
    # version("2.40.0", sha256="49aee8ee447ba0fc1740483ee7dedfbadba800a458a79e71630ff60df0b75ef4")
    # version("2.39.0", sha256="fef2bb41d4ce2c9004612cbed5c2c6c4a2446782c58b557818279d97728d88dc")
    # version("2.38.0", sha256="1579a974ef80eba0796be0fc95e4e7546cb1885cd682c50bf952f498618b8f04")
    # version("2.37.0", sha256="dcf92302ba813080003f33cb874912ee950331f2348822a2b615eb46f9baf0f8")
    # version("2.36.1", sha256="84313cc1cef65614f3ad67fea8deab55998a5534db7bceadb649efdc0739bad3")
    # version("2.36.0", sha256="7413b6974ebfaf2170a648e91c2d1731ac980663fcafe9c1aceb227062c10cea")
    # version("2.35.0", sha256="ce341513458846e070b4247c8c7c86bb6ba7a7832d76f24c31feb41d8e79bacd")
    # version("2.34.0", sha256="7a9798bd4647f4811887d281b28ae019b2859e2ab08fc6ff69b3fc64a4af2d6e")

    variant("default", default=False, description="Install default extras", when="@2")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("bazel@6.5:", type="build")
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
