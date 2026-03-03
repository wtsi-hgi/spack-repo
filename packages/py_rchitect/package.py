# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRchitect(PythonPackage):
    """Interoperate R with Python"""

    homepage = "https://github.com/randy3k/rchitect"
    git = "https://github.com/randy3k/rchitect"

    version("0.4.6", tag="v0.4.6")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))

    depends_on("py-cffi@1.10.0:", type=("build", "run"))
    depends_on("py-six@1.9.0:", type=("build", "run"))
    depends_on("py-packaging@23.0:", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pytest-runner", type=("build", "run"))
    depends_on("py-pytest-mock", type=("build", "run"))
    depends_on("py-pytest-cov", type=("build", "run"))

