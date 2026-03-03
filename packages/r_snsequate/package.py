# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnsequate(RPackage):
	"""Standard and Nonstandard Statistical Models and Methods for Test
Equating

	Contains functions to perform various models and
    methods for test equating. It currently implements the traditional
    mean, linear and equipercentile equating methods. Both IRT observed-score 
    and true-score equating are also supported, as well as the mean-mean, 
    mean-sigma, Haebara and Stocking-Lord IRT linking methods.
    It also supports newest methods such that local equating, kernel
    equating (using Gaussian, logistic, Epanechnikov, uniform and adaptive 
    kernels) with presmoothing, and IRT parameter linking methods based on 
    asymmetric item characteristic functions. Functions to obtain both 
    standard error of equating (SEE) and standard error of equating differences 
    between two equating functions (SEED) are also implemented for the kernel method of
    equating.
	"""
	
	homepage = "https://www.mat.uc.cl/~jorge.gonzalez/"
	cran = "SNSequate" 

	version("1.3-4", md5="fbafe444bb44d4fede1baab5c024886e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
