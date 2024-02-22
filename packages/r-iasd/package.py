# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIasd(RPackage):
	"""Model Selection for Index of Asymmetry Distribution

	Calculate AIC's and AICc's of unimodal model (one normal distribution) and bimodal model(a mixture of two normal distributions) which fit the distribution of indices of asymmetry (IAS), and plot their density, to help determine IAS distribution is unimodal or bimodal.
	"""
	
	cran = "IASD" 

	version("1.1.1", md5="216cdfe0c10493c9c324dbf7522355dc")

