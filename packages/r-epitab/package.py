# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitab(RPackage):
	"""Flexible Contingency Tables for Epidemiology

	Builds contingency tables that cross-tabulate multiple 
    categorical variables and also calculates various summary measures.
    Export to a variety of formats is supported, including: 'HTML', 
    'LaTeX', and 'Excel'.
	"""
	
	homepage = "https://github.com/stulacy/epitab"
	cran = "epitab" 

	version("0.2.2", md5="d969ce8648c4326f51ca713a91a9b9f2")

	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
