# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmapr(RPackage):
    """An R interface to the GMAP/GSNAP/GSTRUCT suite

    GSNAP and GMAP are a pair of tools to align short-read data written by Tom Wu.  This package provides convenience methods to work with GMAP and GSNAP from within R. In addition, it provides methods to tally alignment results on a per-nucleotide basis using the bam_tally tool.
    """

    bioc = "gmapR"

    version("1.50.0", commit="0b5ffd173a80210a53b122a8fe2587fa7d26e325")
    version("1.44.0", commit="5a7a72619365b0a02cdc93a45acb934cc0069706")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
    depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
    depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
    depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
    depends_on("r-iranges@2.13.12:", type=("build", "run"))
    depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
    depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
    depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-variantannotation@1.25.11:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
