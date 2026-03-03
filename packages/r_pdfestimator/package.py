# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdfestimator(RPackage):
	"""Multivariate Nonparametric Probability Density Estimator

	Farmer, J., D. Jacobs (2108) <DOI:10.1371/journal.pone.0196937>. A multivariate nonparametric density estimator based on the maximum-entropy method.  Accurately predicts a probability density function (PDF) for random data using a novel iterative scoring function to determine the best fit without overfitting to the sample. 
	"""
	
	cran = "PDFEstimator" 

	version("4.5", md5="be1d8b1e3c63f7303416183e2d0dc944")

	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-multirng", type=("build", "run"))
