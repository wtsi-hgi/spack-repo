# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROccugene(RPackage):
    """Functions for Multinomial Occupancy Distribution

    Statistical tools for building random mutagenesis libraries for prokaryotes. The package has functions for handling the occupancy distribution for a multinomial and for estimating the number of essential genes in random transposon mutagenesis libraries.
    """

    bioc = "occugene"

    version("1.68.0", commit="0dd2822b271db44dbe05ccad2f0c2390317ba15b")
    version("1.62.0", commit="194ce6a6c735fb18e66a6fe0bd20fd2afd93dd64")

    depends_on("r@2:", type=("build", "run"))
