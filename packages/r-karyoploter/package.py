# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RKaryoploter(RPackage):
    """karyoploteR creates karyotype plots of arbitrary genomes and offers a complete set of functions to plot arbitrary data on them."""

    homepage = "https://github.com/bernatgel/karyoploteR"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/karyoploteR_1.26.0.tar.gz"
    bioc = "karyoploteR"

    version("1.26.0", sha256="1d192cf0b0564d8b1b89710e0e1e6f387824434d45994b94e6a87e45a5a80cdb")

    depends_on("r-regioner", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biovizbase", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-bamsignals", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-memoise", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-bezier", type=("build", "run"))