# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsranks(RPackage):
	"""Statistical Tools for Ranks

	Account for uncertainty when working with ranks. 
    Estimate standard errors consistently in linear regression with ranked variables.
    Construct confidence sets of various kinds for positions of populations in a ranking 
    based on values of a certain feature and their estimation errors. 
    Theory based on Mogstad, Romano, Shaikh, and Wilhelm (2023)<doi:10.1093/restud/rdad006> and
    Chetverikov and Wilhelm (2023) <arXiv:2310.15512>.
	"""
	
	homepage = "https://github.com/danielwilhelm/R-CS-ranks"
	cran = "csranks" 

	version("1.2.2", md5="26470808091c4d47ca558d881298a1da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
