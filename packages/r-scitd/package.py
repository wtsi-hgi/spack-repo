# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScitd(RPackage):
	"""Single-Cell Interpretable Tensor Decomposition

	Single-cell Interpretable Tensor Decomposition (scITD) employs the 
    Tucker tensor decomposition to extract multicell-type gene expression patterns 
    that vary across donors/individuals. This tool is geared for use with single-cell
    RNA-sequencing datasets consisting of many source donors. The method has a wide
    range of potential applications, including the study of inter-individual variation
    at the population-level, patient sub-grouping/stratification, and the analysis
    of sample-level batch effects. Each "multicellular process" that is extracted 
    consists of (A) a multi cell type gene loadings matrix and (B) a
    corresponding donor scores vector indicating the level at which the corresponding
    loadings matrix is expressed in each donor. Additional methods are implemented
    to aid in selecting an appropriate number of factors and to evaluate stability
    of the decomposition. Additional tools are provided for downstream analysis,
    including integration of gene set enrichment analysis and ligand-receptor analysis. 
    Tucker, L.R. (1966) <doi:10.1007/BF02289464>. Unkel, S., Hannachi, A., Trendafilov, N. T., & Jolliffe, I. T. (2011) <doi:10.1007/s13253-011-0055-9>. Zhou, G., & Cichocki, A. (2012) <doi:10.2478/v10175-012-0051-4>.
	"""
	
	cran = "scITD" 

	version("1.0.4", md5="e47580444a1fe8f051631baacf651426")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-sccore", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
