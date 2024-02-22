# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwls(RPackage):
	"""Gene Expression Deconvolution Using Dampened Weighted Least
Squares

	The rapid development of single-cell transcriptomic technologies 
    has helped uncover the cellular heterogeneity within cell populations. 
    However, bulk RNA-seq continues to be the main workhorse for quantifying 
    gene expression levels due to technical simplicity and low cost. To most 
    effectively extract information from bulk data given the new knowledge 
    gained from single-cell methods, we have developed a novel algorithm to 
    estimate the cell-type composition of bulk data from a single-cell 
    RNA-seq-derived cell-type signature. Comparison with existing methods using 
    various real RNA-seq data sets indicates that our new approach is more 
    accurate and comprehensive than previous methods, especially for the 
    estimation of rare cell types. More importantly,our method can detect 
    cell-type composition changes in response to external perturbations, 
    thereby providing a valuable, cost-effective method for dissecting the 
    cell-type-specific effects of drug treatments or condition changes. 
    As such, our method is applicable to a wide range of biological and 
    clinical investigations. Dampened weighted least squares ('DWLS') is an 
    estimation method for gene expression deconvolution, in which the cell-type 
    composition of a bulk RNA-seq data set is computationally inferred. 
    This method corrects common biases towards cell types that are 
    characterized by highly expressed genes and/or are highly prevalent, to 
    provide accurate detection across diverse cell types. See: 
    <https://www.nature.com/articles/s41467-019-10802-z.pdf> for more 
    information about the development of 'DWLS' and the methods behind our 
    functions. 
	"""
	
	homepage = "https://github.com/sistia01/DWLS"
	cran = "DWLS" 

	version("0.1.0", md5="e9f0e2d1303dd5cc1a7fc48ba1d6f1b5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mast", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
