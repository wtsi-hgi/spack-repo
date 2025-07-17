# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpfe(RPackage):
    """Estimation of the amplicon methylation pattern distribution from bisulphite sequencing data

    Estimate distribution of methylation patterns from a table of counts from a bisulphite sequencing experiment given a non-conversion rate and read error rate.
    """

    bioc = "MPFE"

    version("1.44.0", commit="f3510bf41e45e886021d1dac55bf27a02079c5c6")
    version("1.38.0", commit="5beaae5cecd8284a4e649c18e71de7c110b291ee")
