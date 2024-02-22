# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDomir(RPackage):
	"""Tools to Support Relative Importance Analysis

	Methods to apply decomposition-based relative importance 
  analysis for R functions. This package supports the application of 
  decomposition methods by providing 'lapply'- or 'Map'-like meta-functions that 
  compute dominance analysis (Azen, R., & Budescu, D. V. (2003) 
  <doi:10.1037/1082-989X.8.2.129>; Grömping, U. (2007) 
  <doi:10.1198/000313007X188252>) or Shapley value regression 
  (Lipovetsky, S., & Conklin, M. (2001) <doi:10.1002/asmb.446>)
  based on the values returned from other functions.
	"""
	
	homepage = "https://github.com/jluchman/domir"
	cran = "domir" 

	version("1.1.1", md5="c47f9bc5aba06d00befcba4cba976285")

