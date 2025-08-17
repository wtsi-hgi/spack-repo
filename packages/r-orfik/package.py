# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrfik(RPackage):
    """Open Reading Frames in Genomics

    R package for analysis of transcript and translation features through manipulation of sequence data and NGS data like Ribo-Seq, RNA-Seq, TCP-Seq and CAGE. It is generalized in the sense that any transcript region can be analysed, as the name hints to it was made with investigation of ribosomal patterns over Open Reading Frames (ORFs) as it's primary use case. ORFik is extremely fast through use of C++, data.table and GenomicRanges. Package allows to reassign starts of the transcripts with the use of CAGE-Seq data, automatic shifting of RiboSeq reads, finding of Open Reading Frames for whole genomes and much more.
    """

    homepage = "https://github.com/Roleren/ORFik"
    bioc = "ORFik"

    version("1.28.2", commit="87fcbbfdf7216621fc63b88f51d07d9d31ae4dd8")
    version("1.22.2", commit="38d47486f2a2e45f29306b5af1ed21a7be42dc0d")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-iranges@2.17.1:", type=("build", "run"))
    depends_on("r-genomicranges@1.35.1:", type=("build", "run"))
    depends_on("r-genomicalignments@1.19:", type=("build", "run"))
    depends_on("r-annotationdbi@1.45:", type=("build", "run"))
    depends_on("r-biostrings@2.51.1:", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-biomartr@1.0.7:", type=("build", "run"))
    depends_on("r-biocgenerics@0.29.1:", type=("build", "run"))
    depends_on("r-biocparallel@1.19:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-cowplot@1:", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-data-table@1.11.8:", type=("build", "run"))
    depends_on("r-deseq2@1.24:", type=("build", "run"))
    depends_on("r-downloader", type=("build", "run"))
    depends_on("r-fst@0.9.2:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.15.5:", type=("build", "run"))
    depends_on("r-genomicfeatures@1.31.10:", type=("build", "run"))
    depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-httr@1.3:", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rsamtools@1.35:", type=("build", "run"))
    depends_on("r-rtracklayer@1.43:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.14:", type=("build", "run"))
    depends_on("r-s4vectors@0.21.3:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-xml2@1.2:", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    # ORFik imports txdbmaker at runtime for TxDb creation utilities
    depends_on("r-txdbmaker", type=("build", "run"))
