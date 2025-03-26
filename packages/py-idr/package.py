# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-idr
#
# You can edit this file again by typing:
#
#     spack edit py-idr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack.package import *


class PyIdr(PythonPackage):
    """Irreproducible Discovery Rate (IDR) is a framework to measure
    the reproducibility of findings identified from replicate experiments
    and provide highly stable thresholds based on reproducibility."""

    homepage = "https://github.com/nboley/idr"
    git = "https://github.com/nboley/idr.git"

    license("GPL-2.0")

    version("20170623", commit="74665e73bffb689a440948640c386b1188eea1e3")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
