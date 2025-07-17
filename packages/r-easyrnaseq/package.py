# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyrnaseq(RPackage):
    """Count summarization and normalization for RNA-Seq data

    Calculates the coverage of high-throughput short-reads against a genome of reference and summarizes it per feature of interest (e.g. exon, gene, transcript). The data can be normalized as 'RPKM' or by the 'DESeq' or 'edgeR' package.
    """

    bioc = "easyRNASeq"

    version("2.44.0", commit="8c15d8f4a77449eb23010648d0708bb0a38f6b3d")
    version("2.38.0", commit="e7d99c2cdf49653ef0c483bb69d47b2a8ce18d0b")

    depends_on("r-biobase@2.50:", type=("build", "run"))
    depends_on("r-biocfilecache@1.14:", type=("build", "run"))
    depends_on("r-biocgenerics@0.36:", type=("build", "run"))
    depends_on("r-biocparallel@1.24.1:", type=("build", "run"))
    depends_on("r-biomart@2.46:", type=("build", "run"))
    depends_on("r-biostrings@2.58:", type=("build", "run"))
    depends_on("r-edger@3.32:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.26:", type=("build", "run"))
    depends_on("r-genomeintervals@1.46:", type=("build", "run"))
    depends_on("r-genomicalignments@1.26:", type=("build", "run"))
    depends_on("r-genomicranges@1.42:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.20:", type=("build", "run"))
    depends_on("r-iranges@2.24:", type=("build", "run"))
    depends_on("r-lsd@4.1.0:", type=("build", "run"))
    depends_on("r-locfit", type=("build", "run"))
    depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
    depends_on("r-rsamtools@2.6:", type=("build", "run"))
    depends_on("r-s4vectors@0.28:", type=("build", "run"))
    depends_on("r-shortread@1.48:", type=("build", "run"))
