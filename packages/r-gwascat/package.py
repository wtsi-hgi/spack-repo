# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwascat(RPackage):
    """representing and modeling data in the EMBL-EBI GWAS catalog

    Represent and model data in the EMBL-EBI GWAS catalog.
    """

    bioc = "gwascat"

    version("2.40.0", commit="65b07e3b0d6af6d27f0e2b9a59aefcd989f8ebbf")
    version("2.34.0", commit="9252d332d4d7c62d9fe923c7164eb0d1fa69723b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges@1.29.6:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-snpstats", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
