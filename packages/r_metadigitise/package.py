# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetadigitise(RPackage):
	"""Extract and Summarise Data from Published Figures

	High-throughput, flexible and reproducible extraction of data from figures in primary research papers. metaDigitise() can extract data and / or automatically calculate summary statistics for users from box plots, bar plots (e.g., mean and errors), scatter plots and histograms.
	"""
	
	cran = "metaDigitise" 

	version("1.0.1", md5="4daa65eba895957359c94ed9c6afd0d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
