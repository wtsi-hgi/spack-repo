# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumibarnes(RPackage):
    """Barnes Benchmark Illumina Tissues Titration Data

    The Barnes benchmark dataset can be used to evaluate the algorithms for Illumina microarrays. It measured a titration series of two human tissues, blood and placenta, and includes six samples with the titration ratio of blood and placenta as 100:0, 95:5, 75:25, 50:50, 25:75 and 0:100. The samples were hybridized on HumanRef-8 BeadChip (Illumina, Inc) in duplicate. The data is loaded as an LumiBatch Object (see documents in the lumi package).
    """

    bioc = "lumiBarnes"

    version("1.48.0", commit="fbc484c88cda76a402850f8c323b350a4c905874")
    version("1.42.0", commit="8d90ec5d172d6011385fe9563db03b75ee2eaa39")

    depends_on("r@2:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-lumi@1.1:", type=("build", "run"))
