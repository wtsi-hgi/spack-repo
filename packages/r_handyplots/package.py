# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandyplots(RPackage):
	"""Handy Plots

	Several handy plots for quickly looking at the relationship between two numeric vectors of equal length. Quickly visualize scatter plots, residual plots, qq-plots, box plots, confidence intervals, and prediction intervals.
	"""
	
	cran = "handyplots" 

	version("1.1.3", md5="144601050ca72dd0891b346787901677")

	depends_on("r@3.4:", type=("build", "run"))
