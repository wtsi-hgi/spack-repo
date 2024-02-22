# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPodcall(RPackage):
	"""Positive Droplet Calling for DNA Methylation Droplet Digital PCR

	Reads files exported from 'QX Manager or QuantaSoft' containing amplitude values from a run of ddPCR (96 well plate) and robustly sets thresholds to determine positive droplets for each channel of each individual well. Concentration and normalized concentration in addition to other metrics is then calculated for each well. Results are returned as a table, optionally written to file, as well as optional plots (scatterplot and histogram) for both channels per well written to file. The package includes a shiny application which provides an interactive and user-friendly interface to the full functionality of PoDCall.
	"""
	
	bioc = "PoDCall" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PoDCall_1.10.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PoDCall/PoDCall_1.10.1.tar.gz"]

	version("1.10.1", md5="63532d1fbd2dc2d96ef3f3355125efd5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
