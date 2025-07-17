# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmap2data(RPackage):
    """Connectivity Map (version 2) Data

    Data package which provides default drug profiles for the DrugVsDisease package as well as associated gene lists and data clusters used by the DrugVsDisease package.
    """

    bioc = "cMap2data"

    version("1.44.0", commit="ab401ed513864172e14c508ca54e90eb6862b385")
    version("1.38.0", commit="39393da6a237dd70abd087419bd255e99ff2679b")

    depends_on("r@2.10:", type=("build", "run"))
