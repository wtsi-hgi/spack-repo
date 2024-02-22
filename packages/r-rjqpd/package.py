# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjqpd(RPackage):
	"""The Johnson Quantile-Parameterised Distribution

	Implementation of the Johnson Quantile-Parameterised Distribution in R. 
  The Johnson Quantile-Parameterised Distribution (J-QPD) is a flexible distribution
  system that is parameterised by a symmetric percentile triplet of quantile values
  (typically the 10th-50th-90th) along with known support bounds for the distribution.
  The J-QPD system was developed by Hadlock and Bickel (2017) <doi:10.1287/deca.2016.0343>.
  This package implements the density, quantile, CDF and random number generator functions.
	"""
	
	homepage = "https://github.com/bobbyingram/rjqpd"
	cran = "rjqpd" 

	version("0.2.3", md5="9e25dcaa1ea0dcf525066dae10413590")

