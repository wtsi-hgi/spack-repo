# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaicsexample(RPackage):
    """Example data for the mosaics package, which implements MOSAiCS and MOSAiCS-HMM, a statistical framework to analyze one-sample or two-sample ChIP-seq data for transcription factor binding and histone modification

    Data for the mosaics package, consisting of (1) chromosome 22 ChIP and control sample data from a ChIP-seq experiment of STAT1 binding and H3K4me3 modification in MCF7 cell line from ENCODE database (HG19) and (2) chromosome 21 ChIP and control sample data from a ChIP-seq experiment of STAT1 binding, with mappability, GC content, and sequence ambiguity scores of human genome HG18.
    """

    homepage = "http://groups.google.com/group/mosaics_user_group"
    bioc = "mosaicsExample"

    version("1.46.0", commit="57de14601548e4febbd68fd1972d9772c8918a85")
    version("1.40.0", commit="b5f14d574e64b665f2f80c1e3810bdfbaca30d2a")

    depends_on("r@2.11.1:", type=("build", "run"))
