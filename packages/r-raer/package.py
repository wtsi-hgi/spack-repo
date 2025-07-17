# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaer(RPackage):
    """RNA editing tools in R

    Toolkit for identification and statistical testing of RNA editing signals from within R. Provides support for identifying sites from bulk-RNA and single cell RNA-seq datasets, and general methods for extraction of allelic read counts from alignment files. Facilitates annotation and exploratory analysis of editing signals using Bioconductor packages and resources.
    """

    homepage = "https://rnabioco.github.io/raer"
    bioc = "raer"

    version("1.6.0", commit="9c382c203647b84ff0209c7de8b544ac82a59837")
    version("1.0.2", commit="852cee5e58b4d2f1010a2c862f69572ed0bcc788")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-rhtslib", type=("build", "run"))
    depends_on("curl", type=("build", "link", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("xz", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))
