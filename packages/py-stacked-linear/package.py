# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyStackedLinear(PythonPackage):
    """Efficient implementation of stacked linear modules."""

    homepage = "https://github.com/moinfar/stacked-linear"
    pypi = "stacked-linear/stacked_linear-0.2.0.tar.gz"

    license("MIT")

    version("0.2.0", sha256="5baf4f1195ebdfa265b6efeb6f5a4f82ae60f6fd2b663b5cf971aa8222fb9f8b")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-torch@2:", type=("build", "run"))

    def patch(self):
        filter_file(
            '"Programming Language :: Python :: 3.14",\n',
            "",
            "pyproject.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        python = which(self.spec["python"].command.path)
        python("-c", "import stacked_linear")
