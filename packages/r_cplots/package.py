# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCplots(RPackage):
	"""Plots for Circular Data

	Provides functions to produce some circular plots for circular data, in a height- or area-proportional manner. They include bar plots, smooth density plots, stacked dot plots, histograms, multi-class stacked smooth density plots, and multi-class stacked histograms. 
	"""
	
	cran = "cplots" 

	version("0.5-0", md5="6186a9756e9a80018f9a9c4475f27cb2")

	depends_on("r-circular", type=("build", "run"))
