# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqdtu(RPackage):
    """RNA-seq workflow for differential transcript usage following Salmon quantification

    RNA-seq workflow for differential transcript usage (DTU) following Salmon quantification. This workflow uses Bioconductor packages tximport, DRIMSeq, and DEXSeq to perform a DTU analysis on simulated data. It also shows how to use stageR to perform two-stage testing of DTU, a statistical framework to screen at the gene level and then confirm which transcripts within the significant genes show evidence of DTU.
    """

    homepage = "https://github.com/thelovelab/rnaseqDTU/"
    bioc = "rnaseqDTU"

    version("1.28.0", commit="5e81cf1a923d6b5b785bf8eac011da244cdc1d97")
    version("1.22.0", commit="816777f5cac875d6162894dce8fa90d25d84c447")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-drimseq", type=("build", "run"))
    depends_on("r-dexseq", type=("build", "run"))
    depends_on("r-stager", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-rafalib", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
