# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAstrodatr(RPackage):
	"""Astronomical Data

	A collection of 19 datasets from contemporary astronomical research.  They are described the textbook `Modern Statistical Methods for Astronomy with R Applications' by Eric D. Feigelson and G. Jogesh Babu (Cambridge University Press, 2012, Appendix C) or on the website of Penn State's Center for Astrostatistics (http://astrostatistics.psu.edu/datasets).  These datasets can be used to exercise methodology involving: density estimation; heteroscedastic measurement errors; contingency tables; two-sample hypothesis tests; spatial point processes; nonlinear regression; mixture models; censoring and truncation; multivariate analysis; classification and clustering; inhomogeneous Poisson processes; periodic and stochastic time series analysis.  
	"""
	
	cran = "astrodatR" 

	version("0.1", md5="97f3d6476816a37e2bb7aa9ffbd49eb0")

