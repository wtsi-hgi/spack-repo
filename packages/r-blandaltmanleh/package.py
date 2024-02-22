# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlandaltmanleh(RPackage):
	"""Plots (Slightly Extended) Bland-Altman Plots

	Bland-Altman Plots using either base graphics or ggplot2,
    augmented with confidence intervals, with detailed return values and
    a sunflowerplot option for data with ties.
	"""
	
	cran = "BlandAltmanLeh" 

	version("0.3.1", md5="50d200b7bd2d9634112aaa9e49effd2d")

