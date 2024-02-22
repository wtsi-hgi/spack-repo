# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmulticorrdata(RPackage):
	"""Simulation of Correlated Data with Multiple Variable Types

	Generate continuous (normal or non-normal), binary, ordinal, and count (Poisson or Negative 
    Binomial) variables with a specified correlation matrix.  It can also produce a single continuous 
    variable.  This package can be used to simulate data sets that mimic real-world situations (i.e. 
    clinical or genetic data sets, plasmodes).  All variables are generated from standard normal 
    variables with an imposed intermediate correlation matrix.  Continuous variables are simulated 
    by specifying mean, variance, skewness, standardized kurtosis, and fifth and sixth standardized 
    cumulants using either Fleishman's third-order (<DOI:10.1007/BF02293811>) or Headrick's 
    fifth-order (<DOI:10.1016/S0167-9473(02)00072-5>) polynomial transformation.  Binary and 
    ordinal variables are simulated using a modification of the ordsample() function from 'GenOrd'.  
    Count variables are simulated using the inverse cdf method.  There are two simulation pathways 
    which differ primarily according to the calculation of the intermediate correlation matrix.  In 
    Correlation Method 1, the intercorrelations involving count variables are determined using a 
    simulation based, logarithmic correlation correction (adapting Yahav and Shmueli's 2012 method, 
    <DOI:10.1002/asmb.901>).  In Correlation Method 2, the count variables are treated as ordinal 
    (adapting Barbiero and Ferrari's 2015 modification of GenOrd, <DOI:10.1002/asmb.2072>).  
    There is an optional error loop that corrects the final correlation matrix to be within a 
    user-specified precision value of the target matrix.  The package also includes functions to 
    calculate standardized cumulants for theoretical distributions or from real data sets, check 
    if a target correlation matrix is within the possible correlation bounds (given the distributions 
    of the simulated variables), summarize results (numerically or graphically), to verify valid power 
    method pdfs, and to calculate lower standardized kurtosis bounds.
	"""
	
	homepage = "https://github.com/AFialkowski/SimMultiCorrData"
	cran = "SimMultiCorrData" 

	version("0.2.2", md5="3d88259ba6ea91f806899331de99f0a2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
