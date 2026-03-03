# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmahalanobis(RPackage):
	"""Calculate the Mahalanobis Distance for a Given List of Data
Frames with Factors

	It provides a function that calculates the Mahalanobis distance between each pair of species in a list of data frames. Each data frame contains the observations of a species with some factors. Mahalanobis distance is a measure of dissimilarity between two vectors of multivariate random variables, based on the covariance matrix. This distance is useful for statistical matching or fusion of data, that is the integration of two data sources that refer to the same target population and that share some variables.
  - "Fisher, R.A. (1922) On the mathematical foundations of theoretical statistics. <doi:10.1098/rsta.1922.0009>".
  - "Mahalanobis, P.C. (1936) On the generalized distance in statistics. <doi:10.1007/s13171-019-00164-5>".
	"""
	
	cran = "cmahalanobis" 

	version("0.1.0", md5="572ca87f8683171d8639a83895d1cd3d")

