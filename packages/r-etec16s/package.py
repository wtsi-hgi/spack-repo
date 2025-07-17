# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtec16s(RPackage):
    """Individual-specific changes in the human gut microbiota after challenge with enterotoxigenic Escherichia coli and subsequent ciprofloxacin treatment

    16S rRNA gene sequencing data to study changes in the faecal microbiota of 12 volunteers during a human challenge study with ETEC (H10407) and subsequent treatment with ciprofloxacin.
    """

    bioc = "etec16s"

    version("1.36.0", commit="4987d11b96b5bb68cf34ebec6bc1bc388ab623ab")
    version("1.30.0", commit="61dee1a3508d58dedd26afd34be99e88f504eae1")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-metagenomeseq@1.12:", type=("build", "run"))
