# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdadensity(RPackage):
	"""Functional Data Analysis for Density Functions by Transformation
to a Hilbert Space

	An implementation of the methodology described in
    Petersen and Mueller (2016) <doi:10.1214/15-AOS1363> for the functional
    data analysis of samples of density functions.  Densities are first
    transformed to their corresponding log quantile densities, followed by
    ordinary Functional Principal Components Analysis (FPCA).  Transformation
    modes of variation yield improved interpretation of the variability in the
    data as compared to FPCA on the densities themselves.  The standard
    fraction of variance explained (FVE) criterion commonly used for functional
    data is adapted to the transformation setting, also allowing for an
    alternative quantification of variability for density data through the
    Wasserstein metric of optimal transport.
	"""
	
	homepage = "https://github.com/functionaldata/tDENS"
	cran = "fdadensity" 

	version("0.1.2", md5="a8225953b2e9f9c5d0d186a4ec7d6c73")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fdapace@0.3:", type=("build", "run"))
