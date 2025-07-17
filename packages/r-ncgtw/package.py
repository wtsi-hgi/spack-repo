# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcgtw(RPackage):
    """Alignment of LC-MS Profiles by Neighbor-wise Compound-specific Graphical Time Warping with Misalignment Detection

    The purpose of ncGTW is to help XCMS for LC-MS data alignment. Currently, ncGTW can detect the misaligned feature groups by XCMS, and the user can choose to realign these feature groups by ncGTW or not.
    """

    bioc = "ncGTW"

    version("1.22.0", commit="2b9fd345f4694a4b6b28655a12069a2a5bd59ff9")
    version("1.16.0", commit="0d9b8cc2d419f697681cebbdffb1a1c57f6b74e3")

    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-xcms", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
