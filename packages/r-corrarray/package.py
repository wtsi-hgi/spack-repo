# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrarray(RPackage):
	"""Correlation Arrays and 2-Sample Correlation Matrices

	The goal of 'corrarray' is to create a multi-sample
  correlation array by combining the correlation matrices of a data set
  stratified by a grouping variable. 
  For two specified levels of the variable, 'corrarray' displays one level's 
  correlation matrix in the lower triangular matrix and the other level's
  correlation matrix in the upper triangular matrix.
  Such an output can enable visualization of correlations from two samples
  in a single correlation matrix or corrgram.
	"""
	
	homepage = "https://github.com/Medicine1/corrarray"
	cran = "corrarray" 

	version("1.2.0", md5="ce0e807d7074d8780f123c5611d3d8d5")

	depends_on("r-hmisc", type=("build", "run"))
