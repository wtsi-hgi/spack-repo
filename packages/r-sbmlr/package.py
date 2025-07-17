# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbmlr(RPackage):
    """SBML-R Interface and Analysis Tools

    This package contains a systems biology markup language (SBML) interface to R.
    """

    homepage = "http://epbi-radivot.cwru.edu/SBMLR/SBMLR.html"
    bioc = "SBMLR"

    version("2.4.0", commit="ac2b6a556a842d12677b89ac75b06250a7450ed1")
    version("1.98.0", commit="f2c95a07de1f01b2e3541a90fc7e4bd88497818a")

    depends_on("r-xml", type=("build", "run"))
    depends_on("r-desolve", type=("build", "run"))
