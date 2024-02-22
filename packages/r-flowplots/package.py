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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowPlots_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowPlots/flowPlots_1.50.0.tar.gz"]

	version("1.50.0", md5="523b0d79646813f56d711d3e0f38a5e9")

	depends_on("r@2.13:", type=("build", "run"))
