# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyDmslogo(PythonPackage):
    """dmslogo is a Python package written by the Bloom lab for making sequence logo plots to visualize deep mutational scanning data."""

    homepage = "https://github.com/jbloomlab/dmslogo"
    git = "https://github.com/jbloomlab/dmslogo"
    pypi = "dmslogo/dmslogo-0.7.0.tar.gz"

    version("0.7.0", sha256="60100b600effbea54d3e841aba1c51b4148e47d2f06483cf02aa6a06060a1bfb")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-pandas@0.23:", type=("build", "run"))
    depends_on("py-matplotlib@3.8:", type=("build", "run"))
    depends_on("py-palettable", type=("build", "run"))

