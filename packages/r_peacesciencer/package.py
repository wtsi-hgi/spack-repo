# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeacesciencer(RPackage):
	"""Tools and Data for Quantitative Peace Science Research

	These are useful tools and data sets for the study of quantitative 
    peace science. The goal for this package is to include tools and data sets
    for doing original research that mimics well what a user would have to previously
    get from a software package that may not be well-sourced or well-supported.
    Those software bundles were useful the extent to which they encourage replications 
    of long-standing analyses by starting the data-generating process from scratch. However, 
    a lot of the functionality can be done relatively quickly and more transparently
    in the R programming language.
	"""
	
	homepage = "https://github.com/svmiller/peacesciencer/"
	cran = "peacesciencer" 

	version("1.1.0", md5="c97825a5dfde91ed3c1bc49eb02c73fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stevemisc@1.6:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
