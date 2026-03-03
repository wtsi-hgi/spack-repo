# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRadian(PythonPackage):
    """radian is an alternative console for the R program with multiline editing and rich syntax highlight."""

    homepage = "https://github.com/randy3k/radian"
    git = "https://github.com/randy3k/radian"

    version("0.6.12", tag="v0.6.12")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))

    depends_on("py-rchitect", type=("build", "run"))
    depends_on("py-prompt-toolkit@3.0.41:3.1", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
    depends_on("py-coverage", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pexpect", type=("build", "run"))
    depends_on("py-ptyprocess", type=("build", "run"))

