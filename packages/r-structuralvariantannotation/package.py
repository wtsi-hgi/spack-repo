# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructuralvariantannotation(RPackage):
    """Variant annotations for structural variants

    StructuralVariantAnnotation provides a framework for analysis of structural variants within the Bioconductor ecosystem. This package contains contains useful helper functions for dealing with structural variants in VCF format. The packages contains functions for parsing VCFs from a number of popular callers as well as functions for dealing with breakpoints involving two separate genomic loci encoded as GRanges objects.
    """

    bioc = "StructuralVariantAnnotation"

    version("1.24.0", commit="8c42c8cdff2007d155a6c71211422b8d878c89b6")
    version("1.18.0", commit="63814f21346090aacfc83170dfcd1a4921b19743")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
