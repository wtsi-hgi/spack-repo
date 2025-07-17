# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuitar(RPackage):
    """Guitar

    The package is designed for visualization of RNA-related genomic features with respect to the landmarks of RNA transcripts, i.e., transcription starting site, start codon, stop codon and transcription ending site.
    """

    bioc = "Guitar"

    version("2.24.0", commit="fea0fa1be5282964df9be8adccb4c16541514027")
    version("2.18.0", commit="836574b623b1eb0146af4903e02c28e089b01e23")

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
