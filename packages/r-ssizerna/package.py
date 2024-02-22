# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsizerna(RPackage):
	"""Sample Size Calculation for RNA-Seq Experimental Design

	We propose a procedure for sample size calculation while
    controlling false discovery rate for RNA-seq experimental design. Our
    procedure depends on the Voom method proposed for RNA-seq data analysis
    by Law et al. (2014) <DOI:10.1186/gb-2014-15-2-r29> and the sample size 
    calculation method proposed for microarray experiments by Liu and Hwang 
    (2007) <DOI:10.1093/bioinformatics/btl664>. We develop a set of functions
    that calculates appropriate sample sizes for two-sample t-test for RNA-seq
    experiments with fixed or varied set of parameters. The outputs also contain a
    plot of power versus sample size, a table of power at different sample sizes,
    and a table of critical test values at different sample sizes. 
    To install this package, please use 
    'source("http://bioconductor.org/biocLite.R"); biocLite("ssizeRNA")'. 
    For R version 3.5 or greater, please use  
    'if(!requireNamespace("BiocManager", quietly = TRUE)){install.packages("BiocManager")}; BiocManager::install("ssizeRNA")'.
	"""
	
	cran = "ssizeRNA" 

	version("1.3.2", md5="f3566b3d83d2838cf957cf2fc92e6494")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-ssize-fdr", type=("build", "run"))
