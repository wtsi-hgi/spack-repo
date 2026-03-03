# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorona(RPackage):
	"""Coronavirus ('Rona') Data Exploration

	Manipulate and view coronavirus data and other societally relevant data at a basic level.
	"""
	
	cran = "corona" 

	version("0.3.0", md5="502ccf7c456306f3a5ab88636a1b94bb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-qicharts2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
