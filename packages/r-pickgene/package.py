# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPickgene(RPackage):
    """Adaptive Gene Picking for Microarray Expression Data Analysis

    Functions to Analyze Microarray (Gene Expression) Data.
    """

    homepage = "http://www.stat.wisc.edu/~yandell/statgen"
    bioc = "pickgene"

    version("1.80.0", commit="b3dac51572de807dd7112b94b8c923ca6883886f")
    version("1.74.0", commit="f8683d09218ba03a492460e542dd656959c05a2e")

    depends_on("r-mass", type=("build", "run"))
