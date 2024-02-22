# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenintro(RPackage):
	"""Data Sets and Supplemental Functions from 'OpenIntro' Textbooks
and Labs

	Supplemental functions and data for 'OpenIntro' resources, which 
    includes open-source textbooks and resources for introductory statistics 
    (<https://www.openintro.org/>). The package contains data sets used in our 
    open-source textbooks along with custom plotting functions for reproducing 
    book figures. Note that many functions and examples include color 
    transparency; some plotting elements may not show up properly (or at all) 
    when run in some versions of Windows operating system.
	"""
	
	homepage = "http://openintrostat.github.io/openintro/"
	cran = "openintro" 

	version("2.4.0", md5="2418c6ee8ad0528d43ba6050092a4b2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-airports", type=("build", "run"))
	depends_on("r-cherryblossom", type=("build", "run"))
	depends_on("r-usdata", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
