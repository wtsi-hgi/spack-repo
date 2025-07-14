# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowplots(RPackage):
	"""flowPlots: analysis plots and data class for gated flow cytometry data

	Graphical displays with embedded statistical tests for gated ICS flow cytometry data, and a data class which stores "stacked" data and has methods for computing summary measures on stacked data, such as marginal and polyfunctional degree data.
	"""
	
	bioc = "flowPlots"

	version("1.56.0", commit="3433082bf19443212230fb3dfa94a0400ec74e12")
	version("1.50.0", commit="18405d0fc4dc6a19e93904cdc48bb25e7baff798")

	depends_on("r@2.13:", type=("build", "run"))
