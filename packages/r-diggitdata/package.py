# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiggitdata(RPackage):
    """Example data for the diggit package

    This package provides expression profile and CNV data for glioblastoma from TCGA, and transcriptional and post-translational regulatory networks assembled with the ARACNe and MINDy algorithms, respectively.
    """

    bioc = "diggitdata"

    version("1.40.0", commit="4925836651e0c3f2d195fa10708ebedeb7dce64f")
    version("1.34.0", commit="1fabf259f128a81ea5d54049206f2f25d1fb2362")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-viper", type=("build", "run"))
