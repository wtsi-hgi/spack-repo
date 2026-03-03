# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoppcr(RPackage):
	"""Classify Digital PCR Droplets by Fitting Fluorescence
Populations

	Estimates DNA target concentration by classifying digital PCR (polymerase chain reaction) droplets as positive, negative, or rain, using Expectation-Maximization Clustering. The fitting is accomplished using the 'EMMIXskew' R package (v. 1.0.3) by Kui Wang, Angus Ng, and Geoff McLachlan (2018) as based on their paper "Multivariate Skew t Mixture Models: Applications to Fluorescence-Activated Cell Sorting Data" <doi:10.1109/DICTA.2009.88>.
	"""
	
	cran = "popPCR" 

	version("0.1.1.1", md5="19298f2c43719dfcbf8e79e30a1ed1e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
