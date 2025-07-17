# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrganismDplyr(RPackage):
    """dplyr-based Access to Bioconductor Annotation Resources

    This package provides an alternative interface to Bioconductor 'annotation' resources, in particular the gene identifier mapping functionality of the 'org' packages (e.g., org.Hs.eg.db) and the genome coordinate functionality of the 'TxDb' packages (e.g., TxDb.Hsapiens.UCSC.hg38.knownGene).
    """

    bioc = "Organism.dplyr"

    version("1.36.0", commit="ce6ab7df6df3c08e501b4e4d3c252d4b1ac1772c")
    version("1.30.1", commit="78e66c1005717f942c0c2d3b06b3d0df738ecaeb")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-dplyr@0.7:", type=("build", "run"))
    depends_on("r-annotationfilter@1.1.3:", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
