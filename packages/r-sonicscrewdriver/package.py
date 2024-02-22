# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSonicscrewdriver(RPackage):
	"""Bioacoustic Analysis and Publication Tools

	Provides basic tools for manipulating sound files for bioacoustic analysis, and preparing analyses these for publication. The package validates that values are physically possible wherever feasible. 
	"""
	
	cran = "sonicscrewdriver" 

	version("0.0.4", md5="03d5f7e7c160bebd580d9959216b71d1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
