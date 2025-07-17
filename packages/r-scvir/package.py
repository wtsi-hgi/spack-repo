# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScvir(RPackage):
    """experimental inferface from R to scvi-tools

    This package defines interfaces from R to scvi-tools.  A vignette works through the totalVI tutorial for analyzing CITE-seq data.  Another vignette compares outputs of Chapter 12 of the OSCA book with analogous outputs based on totalVI quantifications. Future work will address other components of scvi-tools, with a focus on building understanding of probabilistic methods based on variational autoencoders.
    """

    homepage = "https://github.com/vjcitn/scviR"
    bioc = "scviR"

    version("1.8.0", commit="a4f406f3cc15772762e7567b838c0a460c86f0d1")
    version("1.2.0", commit="2a594ba204f383827cf14203038fcebb6184db6b")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
