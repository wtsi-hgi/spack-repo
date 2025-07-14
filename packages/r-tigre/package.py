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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tigre_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tigre/tigre_1.56.0.tar.gz"]

    version("1.62.0", tag="RELEASE_3_21")
	version("1.56.0", sha256="5d212c693c1c061976ab79dada6b1c3f373e4c63a9cc0b5fb049f88fe775c6f2")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
