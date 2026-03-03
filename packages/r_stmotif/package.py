# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmotif(RPackage):
	"""Discovery of Motifs in Spatial-Time Series

	Allow to identify motifs in spatial-time series. A motif is a previously unknown subsequence of a (spatial) time series with relevant number of occurrences. For this purpose, the Combined Series Approach (CSA) is used.
	"""
	
	homepage = "https://github.com/heraldoborges/STMotif/wiki"
	cran = "STMotif" 

	version("2.0.2", md5="e7e39bf75d087f71acccda43cead03a0")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
