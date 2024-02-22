# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaireddata(RPackage):
	"""Paired Data Analysis

	Many datasets and a set of graphics (based on ggplot2), statistics, effect sizes and hypothesis tests are provided for analysing paired data with S4 class.
	"""
	
	cran = "PairedData" 

	version("1.1.1", md5="204ac497b86ee1503275274f5682bd54")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gld", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
