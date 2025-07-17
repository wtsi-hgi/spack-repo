# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedCordbloodnorway450k(RPackage):
    """Illumina HumanMethylation data on sorted cord blood cell populations

    Raw data objects for the Illumina 450k DNA methylation microarrays, for cell type composition estimation.
    """

    homepage = "https://bitbucket.com/kasperdanielhansen/Illumina_CordBlood"
    bioc = "FlowSorted.CordBloodNorway.450k"

    version("1.34.0", commit="95eacd1d4dc0a7f633e0cf717fb06ffaf6454a31")
    version("1.28.0", commit="b9cee45738ff5a791eeef53146d97179f5cf4339")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.21.2:", type=("build", "run"))
