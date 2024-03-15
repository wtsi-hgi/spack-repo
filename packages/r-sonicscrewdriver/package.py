# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSonicscrewdriver(RPackage):
	"""Bioacoustic Analysis and Publication Tools

	Provides tools for manipulating sound files for bioacoustic
  analysis, and preparing analyses these for publication. The package validates
  that values are physically possible wherever feasible. 
	"""
	
	homepage = "https://sonicscrewdriver.ebaker.me.uk"
	cran = "sonicscrewdriver" 

	version("0.0.6", md5="112e26a795d779300ebae20a42a6220d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
