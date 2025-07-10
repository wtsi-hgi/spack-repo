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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scviR_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scviR/scviR_1.2.0.tar.gz"]

	version("1.2.0", sha256="0a15def9dcf1483c867cf45a795b14da37ac97aa686a29e50d2fda5b55475fd9")

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
