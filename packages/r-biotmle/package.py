# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotmle(RPackage):
	"""Targeted Learning with Moderated Statistics for Biomarker Discovery

	Tools for differential expression biomarker discovery based on microarray and next-generation sequencing data that leverage efficient semiparametric estimators of the average treatment effect for variable importance analysis. Estimation and inference of the (marginal) average treatment effects of potential biomarkers are computed by targeted minimum loss-based estimation, with joint, stable inference constructed across all biomarkers using a generalization of moderated statistics for use with the estimated efficient influence function. The procedure accommodates the use of ensemble machine learning for the estimation of nuisance functions.
	"""
	
	homepage = "https://code.nimahejazi.org/biotmle"
	bioc = "biotmle" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biotmle_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biotmle/biotmle_1.26.0.tar.gz"]

	version("1.26.0", sha256="deedd95e7451ea67870c9b8e716bcc8729b5d77055cd886aea7cbbb3bb36e940")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-superheat", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-drtmle@1.0.4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
