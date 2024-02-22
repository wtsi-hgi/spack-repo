# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaupro(RPackage):
	"""Gaussian Process Fitting

	Fits a Gaussian process model to data. Gaussian processes
 are commonly used in computer experiments to fit an interpolating model.
 The model is stored as an 'R6' object and can be easily updated with new 
 data. There are options to run in parallel, and 'Rcpp'
 has been used to speed up calculations.
 For more info about Gaussian process software, see Erickson et al. (2018)
 <doi:10.1016/j.ejor.2017.10.002>.
	"""
	
	homepage = "https://github.com/CollinErickson/GauPro"
	cran = "GauPro" 

	version("0.2.11", md5="7b83fcb15858297bad1dd9865aa12c10")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
