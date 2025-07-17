# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedDlpfc450k(RPackage):
    """Illumina HumanMethylation data on sorted frontal cortex cell populations

    Raw data objects for the Illumina 450k DNA methylation microarrays.
    """

    bioc = "FlowSorted.DLPFC.450k"

    version("1.44.0", commit="b6d17ffc54eebf0f4ec5cc2523caac7405217503")
    version("1.38.0", commit="b5b90bb3d4be912181d46caf138b03cc2dfac83a")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.21.2:", type=("build", "run"))
