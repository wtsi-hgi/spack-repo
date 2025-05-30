# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTretools(PythonPackage):
    """A Python package for data manipulation and cleaning in the TRE (Trusted Research Environment)."""

    homepage = "https://github.com/genes-and-health/tre-tools"
    git = "https://github.com/genes-and-health/tre-tools.git"

    license("MIT")

    version("0.2.0", tag="v0.2.0-release")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-polars", type=("build", "run"))
    depends_on("justbuild", type=("build", "run"))
