# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3cseq(RPackage):
    """Analysis of Chromosome Conformation Capture and Next-generation Sequencing (3C-seq)

    This package is used for the analysis of long-range chromatin interactions from 3C-seq assay.
    """

    homepage = "http://r3cseq.genereg.net"
    bioc = "r3Cseq"

    version("1.54.0", commit="3dc2e20bf43bab28241c16dc6ace45b93e6e2b77")
    version("1.48.0", commit="d9ef32a30102360add6ebc6ff347cb1564a39eb3")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
