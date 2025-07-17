# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelloranges(RPackage):
    """Introduce *Ranges to bedtools users

    Translates bedtools command-line invocations to R code calling functions from the Bioconductor *Ranges infrastructure. This is intended to educate novice Bioconductor users and to compare the syntax and semantics of the two frameworks.
    """

    bioc = "HelloRanges"

    version("1.34.0", commit="6927ba9e27b67fc9183e7e472904bca89510aa67")
    version("1.28.0", commit="8cafa1f566252740491d6589690bf621f93cfbc5")

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.17.39:", type=("build", "run"))
    depends_on("r-iranges@2.13.12:", type=("build", "run"))
    depends_on("r-genomicranges@1.31.10:", type=("build", "run"))
    depends_on("r-biostrings@2.41.3:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomicfeatures@1.31.5:", type=("build", "run"))
    depends_on("r-variantannotation@1.19.3:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicalignments@1.15.7:", type=("build", "run"))
    depends_on("r-rtracklayer@1.33.8:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-docopt", type=("build", "run"))
