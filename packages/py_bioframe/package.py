# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBioframe(PythonPackage):
    """Bioframe is a library to enable flexible and scalable operations on genomic interval dataframes in python. Building bioframe directly on top of pandas enables immediate access to a rich set of dataframe operations. Working in python enables rapid visualization (e.g. matplotlib, seaborn) and iteration of genomic analyses."""

    homepage = "https://github.com/open2c/bioframe"
    pypi = "bioframe/bioframe-0.5.1.tar.gz"

    version("0.5.1", sha256="416132f14334f3921d700a692bf94ea21161ca608e5e3b9a119f97c01012d578")

    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy@1.10:", type=("build", "run"))
    depends_on("py-pandas@1.3:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-hatchling", type=("build", "run"))
