# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWinnerscurse(RPackage):
    """Winner's curse adjustment methods for summary statistics from genome-wide
    association studies."""

    homepage = "https://amandaforde.github.io/winnerscurse/"
    git = "https://github.com/amandaforde/winnerscurse.git"

    license("MIT")

    version("20240307", commit="2ed00bb119a5445e6a2985c0b6bf37a3068b9560")

    depends_on("r", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-scam", type=("build", "run"))
