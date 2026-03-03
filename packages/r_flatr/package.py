# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlatr(RPackage):
	"""Transforms Contingency Tables to Data Frames, and Analyses Them

	Contingency Tables are a pain to work with when you want to run regressions.
  This package takes them, flattens them into a long data frame, so you can more easily analyse them!
  As well, you can calculate other related statistics. All of this is done so in a 'tidy' manner,
  so it should tie in nicely with 'tidyverse' series of packages.
	"""
	
	cran = "flatr" 

	version("0.1.1", md5="a70393b418bcffe95baa75814c823da3")

	depends_on("r@3.4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
