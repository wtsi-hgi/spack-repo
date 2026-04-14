# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryProto(PythonPackage):
    """Generated OpenTelemetry protocol buffer messages for Python."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-proto"
    pypi = "opentelemetry-proto/opentelemetry_proto-1.33.0.tar.gz"

    license("Apache-2.0")

    version("1.33.0", sha256="ec5aa35486c990207ead2512a8d616d1b324928562c91dbc7e0cb9aa48c60b7b")
    version("1.27.0", sha256="33c9345d91dafd8a74fc3d7576c5a38f18b7fdf8d02983ac67485386132aedd6")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-protobuf@3.19:4", when="@1.27.0", type=("build", "run"))
    depends_on("py-protobuf@5:5", when="@1.33.0", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import opentelemetry.proto")
