# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedBlood450k(RPackage):
    """Illumina HumanMethylation data on sorted blood cell populations

    Raw data objects for the Illumina 450k DNA methylation microarrays, and an object depicting which CpGs on the array are associated with cell type.
    """

    bioc = "FlowSorted.Blood.450k"

    version("1.46.0", commit="772690bc1a66161bb55d60258c56785346ad2a12")
    version("1.40.0", commit="7866ba6a249e4686429ba4089f82e71b39b1bf90")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.21.2:", type=("build", "run"))
