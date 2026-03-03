# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for
# details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLegendkit(PythonPackage):
    """Legend creation and manipulation helpers for Matplotlib."""

    homepage = "https://github.com/Marsilea-viz/legendkit"
    pypi = "legendkit/legendkit-0.3.6.tar.gz"

    license("MIT")

    version("0.3.6", sha256="89c0d95c262420086f08c1fff06f9d3d3ee779cacf598464bec7bca10ac36853")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-matplotlib", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import legendkit")
