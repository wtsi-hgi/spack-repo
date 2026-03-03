# Copyright 2013-2023 Lawrence Livermmore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for
# details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUvDynamicVersioning(PythonPackage):
    """Hatch/UV plugin that injects dynamic project versions at build time."""

    homepage = "https://github.com/ninoseki/uv-dynamic-versioning"
    pypi = "uv-dynamic-versioning/uv_dynamic_versioning-0.13.0.tar.gz"

    license("MIT")

    version("0.13.0", sha256="3220cbf10987d862d78e9931957782a274fa438d33efb1fa26b8155353749e06")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling@1.26:", type=("build", "run"))
    depends_on("py-dunamai@1.25:", type=("build", "run"))
    depends_on("py-jinja2@3:", type=("build", "run"))
    depends_on("py-tomlkit@0.13:0.13", type=("build", "run"))

    def patch(self):
        filter_file(
            r'\s*"Programming Language :: Python :: 3\.14",?\n',
            "",
            "pyproject.toml",
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import uv_dynamic_versioning")
