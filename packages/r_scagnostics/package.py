# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScagnostics(RPackage):
	"""Compute scagnostics - scatterplot diagnostics

	Calculates graph theoretic scagnostics. Scagnostics describe various measures of interest for pairs of variables, based on their appearance on a scatterplot.  They are useful tool for discovering interesting or unusual scatterplots from a scatterplot matrix, without having to look at every individual plot.
	"""
	
	homepage = "https://www.rforge.net/scagnostics/"
	cran = "scagnostics" 

	version("0.2-6", md5="dc67096e6075b3ae7d93fc10c1f01aa4")

	depends_on("r-rjava", type=("build", "run"))
