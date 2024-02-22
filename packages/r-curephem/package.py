# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurephem(RPackage):
	"""NPMLE for Logistic-Cox Cure-Rate Model

	Expectation-Maximization (EM) algorithm for point estimation and variance estimation to
    the nonparametric maximum likelihood estimator (NPMLE) for 
    logistic-Cox cure-rate model with left truncation and right-
    censoring. See Hou, Chambers and Xu (2017) <doi:10.1007/s10985-017-9415-2>. 
	"""
	
	cran = "curephEM" 

	version("0.3.0", md5="7cebc1af2f4b5ca768a5a65e12443249")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
