# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsmisc(RPackage):
	"""Data Science Box of Pandora Miscellaneous

	Tool collection for common and not so common data science use cases. This includes 
    custom made algorithms for data management as well as value calculations that are hard to find 
    elsewhere because of their specificity but would be a waste to get lost nonetheless. 
    Currently available functionality: find
    sub-graphs in an edge list data.frame, find mode or modes in a vector of values, extract 
    (a) specific regular expression group(s), generate ISO time stamps that play well with 
    file names, or generate URL parameter lists by expanding value combinations. 
	"""
	
	cran = "dsmisc" 

	version("0.3.3", md5="f41684bef7946946dcb52f929d184013")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
