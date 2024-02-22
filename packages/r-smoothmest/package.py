# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothmest(RPackage):
	"""Smoothed M-Estimators for 1-Dimensional Location

	Some M-estimators for 1-dimensional location (Bisquare,
             ML for the Cauchy distribution, and the estimators from 
             application of the smoothing principle introduced in Hampel, 
             Hennig and Ronchetti (2011) to the above, the Huber
             M-estimator, and the median, main function is smoothm), 
             and Pitman estimator.
	"""
	
	homepage = "https://www.unibo.it/sitoweb/christian.hennig/en"
	cran = "smoothmest" 

	version("0.1-3", md5="5f7a7f615e7008170f8ba3ded007ea94")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
