# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFancova(RPackage):
	"""Nonparametric Analysis of Covariance

	A collection of R functions to perform nonparametric 
    analysis of covariance for regression curves or surfaces. 
    Testing the equality or parallelism of nonparametric curves 
    or surfaces is equivalent to analysis of variance (ANOVA) or 
    analysis of covariance (ANCOVA) for one-sample functional data. 
    Three different testing methods are available in the package, 
    including one based on L-2 distance, one based on an ANOVA 
    statistic, and one based on variance estimators.
	"""
	
	cran = "fANCOVA" 

	version("0.6-1", md5="170092ecbafffe6447d3fe583e8a7fa0")

