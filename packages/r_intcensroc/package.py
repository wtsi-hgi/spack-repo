# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntcensroc(RPackage):
	"""AUC Estimation of Interval Censored Survival Data

	The kernel of this 'Rcpp' based package is an efficient implementation of the generalized gradient projection method for spline function based constrained maximum likelihood estimator for interval censored survival data (Wu, Yuan; Zhang, Ying. Partially monotone tensor spline estimation of the joint distribution function with bivariate current status data. Ann. Statist. 40, 2012, 1609-1636 <doi:10.1214/12-AOS1016>). The key function computes the density function of the joint distribution of event time and the marker and returns the receiver operating characteristic (ROC) curve for the interval censored survival data as well as area under the curve (AUC). 
	"""
	
	homepage = "https://gitlab.oit.duke.edu/dcibioinformatics/soft/intcensroc"
	cran = "intcensROC" 

	version("0.1.3", md5="cd053c8dd6b932598cde69f4f0031951")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
