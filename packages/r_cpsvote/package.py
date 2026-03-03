# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpsvote(RPackage):
	"""A Toolbox for Using the CPS’s Voting and Registration Supplement

	Provides automated methods for downloading, recoding, and merging 
    selected years of the Current Population Survey's Voting and Registration 
    Supplement, a large N national survey about registration, voting, and 
    non-voting in United States federal elections. Provides documentation for 
    appropriate use of sample weights to generate statistical estimates, 
    drawing from Hur & Achen (2013) <doi:10.1093/poq/nft042> and McDonald (2018) 
    <http://www.electproject.org/home/voter-turnout/voter-turnout-data>.
	"""
	
	homepage = "https://github.com/Reed-EVIC/cpsvote"
	cran = "cpsvote" 

	version("0.1.0", md5="953bd9156583c28b23663939f526859c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
