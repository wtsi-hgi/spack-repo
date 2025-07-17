# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLola(RPackage):
    """Locus overlap analysis for enrichment of genomic ranges

    Provides functions for testing overlap of sets of genomic regions with public and custom region set (genomic ranges) databases. This makes it possible to do automated enrichment analysis for genomic region sets, thus facilitating interpretation of functional genomics and epigenomics data.
    """

    homepage = "http://code.databio.org/LOLA"
    bioc = "LOLA"

    version("1.38.0", commit="7bc27064e1478cd0c9e3dd2e6276f8f1ca4cad66")
    version("1.32.0", commit="148d0c13541d60d23001379c377d726d46e51bae")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
