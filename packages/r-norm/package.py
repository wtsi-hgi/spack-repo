# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNorm(RPackage):
	"""Analysis of Multivariate Normal Datasets with Missing Values

	An integrated set of functions for the analysis of 
  multivariate normal datasets with missing values, including implementation of
  the EM algorithm, data augmentation, and multiple imputation.
	"""
	
	cran = "norm" 

	version("1.0-11.1", md5="727b4fa17f06231ab8368630d40d2609")

