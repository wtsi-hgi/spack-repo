# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdm(RPackage):
	"""Quantify Dependence using Rearranged Dependence Measures

	Estimates the rearranged dependence measure ('RDM') of two continuous random variables for different underlying measures. 
  Furthermore, it provides a method to estimate the (SI)-rearrangement copula using empirical checkerboard copulas.
  It is based on the theoretical results presented in Strothmann et al. (2022) <arXiv:2201.03329> and Strothmann (2021) <doi:10.17877/DE290R-22733>.
	"""
	
	homepage = "https://github.com/ChristopherStrothmann/RDM"
	cran = "RDM" 

	version("0.1.1", md5="51e58530d46ffd27cb3978d9208d392b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rfast@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
