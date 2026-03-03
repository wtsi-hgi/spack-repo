# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROaplots(RPackage):
	"""OpenAnalytics Plots Package

	Offers a suite of functions for enhancing R plots.
	"""
	
	homepage = "http://www.openanalytics.eu"
	cran = "oaPlots" 

	version("0.0.25", md5="5e12be6f07bace077e6344ad7d944c6a")

	depends_on("r-oacolors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
