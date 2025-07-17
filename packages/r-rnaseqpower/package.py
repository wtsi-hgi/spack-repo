# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqpower(RPackage):
    """Sample size for RNAseq studies

    RNA-seq, sample size
    """

    bioc = "RNASeqPower"

    version("1.48.0", commit="8c40b86e3f29fcc752858a10dd192105787e3134")
    version("1.42.0", commit="f0b73085c9f6697c0b8ffd34e33280949f5d3abb")
