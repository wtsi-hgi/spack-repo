# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafevote(RPackage):
	"""Election Vote Counting with Safety Features

	Fork of 'vote_2.3-2', Raftery et al. (2021)
  <DOI:10.32614/RJ-2021-086>, with additional support 
  for stochastic experimentation.
	"""
	
	homepage = "https://cthombor.github.io/SafeVote/"
	cran = "SafeVote" 

	version("1.0.0", md5="980e53b9de0c29f97307d3e32cec9389")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
