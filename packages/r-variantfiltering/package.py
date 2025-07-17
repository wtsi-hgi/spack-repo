# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariantfiltering(RPackage):
    """Filtering of coding and non-coding genetic variants

    Filter genetic variants using different criteria such as inheritance model, amino acid change consequence, minor allele frequencies across human populations, splice site strength, conservation, etc.
    """

    homepage = "https://github.com/rcastelo/VariantFiltering"
    bioc = "VariantFiltering"

    version("1.44.0", commit="b610adf0c1f75c900b678e079d4316e52a973fef")
    version("1.38.0", commit="fa37d53a9a0481742d4e9dc3f68b6b294aad3c44")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
    depends_on("r-variantannotation@1.13.29:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomeinfodb@1.3.6:", type=("build", "run"))
    depends_on("r-genomicranges@1.19.13:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-rsamtools@1.17.8:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomicscores@1:", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-shinytree", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
