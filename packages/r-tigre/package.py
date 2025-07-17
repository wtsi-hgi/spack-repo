# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigre(RPackage):
    """Transcription factor Inference through Gaussian process Reconstruction of Expression

    The tigre package implements our methodology of Gaussian process differential equation models for analysis of gene expression time series from single input motif networks. The package can be used for inferring unobserved transcription factor (TF) protein concentrations from expression measurements of known target genes, or for ranking candidate targets of a TF.
    """

    homepage = "https://github.com/ahonkela/tigre"
    bioc = "tigre"

    version("1.62.0", commit="1443c57c0af82a5d0bd58b7e63d4f4ec3cad2dd4")
    version("1.56.0", commit="f92dc572bd3f30298186341815580ce485b54003")

    depends_on("r@2.11:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
