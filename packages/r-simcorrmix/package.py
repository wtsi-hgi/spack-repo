# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcorrmix(RPackage):
	"""Simulation of Correlated Data with Multiple Variable Types
Including Continuous and Count Mixture Distributions

	Generate continuous (normal, non-normal, or mixture distributions), binary, ordinal, 
    and count (regular or zero-inflated, Poisson or Negative Binomial) variables with a specified 
    correlation matrix, or one continuous variable with a mixture distribution.  This package can 
    be used to simulate data sets that mimic real-world clinical or genetic data sets (i.e., 
    plasmodes, as in Vaughan et al., 2009 <DOI:10.1016/j.csda.2008.02.032>).  The methods 
    extend those found in the 'SimMultiCorrData' R package.  Standard normal variables with an 
    imposed intermediate correlation matrix are transformed to generate the desired distributions.  
    Continuous variables are simulated using either Fleishman (1978)'s third order 
    <DOI:10.1007/BF02293811> or Headrick (2002)'s fifth order 
    <DOI:10.1016/S0167-9473(02)00072-5> polynomial transformation method (the power method 
    transformation, PMT).  Non-mixture distributions require the user to specify mean, variance, 
    skewness, standardized kurtosis, and standardized fifth and sixth cumulants.  Mixture 
    distributions require these inputs for the component distributions plus the mixing 
    probabilities.  Simulation occurs at the component level for continuous mixture 
    distributions.  The target correlation matrix is specified in terms of correlations with 
    components of continuous mixture variables.  These components are transformed into the 
    desired mixture variables using random multinomial variables based on the mixing 
    probabilities.  However, the package provides functions to approximate expected correlations 
    with continuous mixture variables given target correlations with the components. Binary and 
    ordinal variables are simulated using a modification of ordsample() in package 'GenOrd'.  
    Count variables are simulated using the inverse CDF method.  There are two simulation 
    pathways which calculate intermediate correlations involving count variables differently.  
    Correlation Method 1 adapts Yahav and Shmueli's 2012 method <DOI:10.1002/asmb.901> and 
    performs best with large count variable means and positive correlations or small means and 
    negative correlations.  Correlation Method 2 adapts Barbiero and Ferrari's 2015 
    modification of the 'GenOrd' package <DOI:10.1002/asmb.2072> and performs best under the 
    opposite scenarios.  The optional error loop may be used to improve the accuracy of the 
    final correlation matrix.  The package also contains functions to calculate the 
    standardized cumulants of continuous mixture distributions, check parameter inputs, 
    calculate feasible correlation boundaries, and summarize and plot simulated variables.
	"""
	
	homepage = "https://github.com/AFialkowski/SimCorrMix"
	cran = "SimCorrMix" 

	version("0.1.1", md5="2c2a06ab94ee0c12ec8c6b76d08ae4ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-simmulticorrdata@0.2.1:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
