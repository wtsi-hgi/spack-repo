# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopyneutralima(RPackage):
    """Copy Neutral Illumina Methylation Arrays

    Provides a set of genomic copy neutral samples hybridized using Illumina Methylation arrays (450k and EPIC).
    """

    bioc = "CopyNeutralIMA"

    version("1.26.0", commit="052f9ffb6577db1f3963ea67526528a2106aa72b")
    version("1.20.0", commit="3b2f5c87cacee086a0b9a55e5cf3457408633f99")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-rdpack@0.8:", type=("build", "run"))
