# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotation(RPackage):
    """Genomic Annotation Resources

    Annotation resources make up a significant proportion of the Bioconductor project. And there are also a diverse set of online resources available which are accessed using specific packages.  This walkthrough will describe the most popular of these resources and give some high level examples on how to use them.
    """

    homepage = "http://bioconductor.org/packages/annotation"
    bioc = "annotation"

    version("1.32.0", commit="05a0ccf03f3362a8e8dd4b6dd7c16437a12e6590")
    version("1.26.0", commit="02f76c2a64e88c3f1532541e216d6abffa271c5a")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-organism-dplyr", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
    depends_on("r-txdb-mmusculus-ucsc-mm10-ensgene", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-homo-sapiens", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-txdb-athaliana-biomart-plantsmart22", type=("build", "run"))
