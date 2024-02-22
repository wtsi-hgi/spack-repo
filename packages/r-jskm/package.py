# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJskm(RPackage):
	"""Kaplan-Meier Plot with 'ggplot2'

	The function 'jskm()' creates publication quality Kaplan-Meier plot with at risk tables below. 'svyjskm()' provides plot for weighted Kaplan-Meier estimator. 
	"""
	
	homepage = "https://github.com/jinseob2kim/jskm"
	cran = "jskm" 

	version("0.5.3", md5="c1b025ed2085d6504084f62cc54346c9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
