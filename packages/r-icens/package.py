# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcens(RPackage):
    """NPMLE for Censored and Truncated Data

    Many functions for computing the NPMLE for censored and truncated data.
    """

    bioc = "Icens"

    version("1.80.0", commit="b90c8140297ff259cc45d8d277705d8ebf2caa8e")
    version("1.74.0", commit="2bca0b3dc24d49baeef3a0bad3a03653ed5667b5")

    depends_on("r-survival", type=("build", "run"))
