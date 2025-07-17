# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfeaChip(RPackage):
    """Analyze Transcription Factor Enrichment

    Package to analize transcription factor enrichment in a gene set using data from ChIP-Seq experiments.
    """

    bioc = "TFEA.ChIP"

    version("1.28.0", commit="129c11f8dda4688d6bdb23a7bd701193fd7e70c1")
    version("1.22.0", commit="fdae2554599851cd6873b0b3f0c1017474bd3664")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
