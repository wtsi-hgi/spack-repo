# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogihist(RPackage):
	"""Combined Graphs for Logistic Regression

	Provides histograms, boxplots and dotplots as alternatives to scatterplots of data when plotting fitted logistic regressions.
	"""
	
	cran = "logihist" 

	version("1.0", md5="45f13312eac90f1cf620798deeeb55f5")

	depends_on("r-ggplot2", type=("build", "run"))
