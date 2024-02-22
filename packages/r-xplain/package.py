# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXplain(RPackage):
	"""Providing Interactive Interpretations and Explanations of
Statistical Results

	Allows to provide live interpretations and explanations of statistical 
    functions in R. These interpretations and explanations are shown when the explained function 
    is called by the user. They can interact with the values of the explained function's actual 
    results to offer relevant, meaningful insights. The 'xplain' interpretations and explanations 
    are based on an easy-to-use XML format that allows to include R code to interact with the 
    returns of the explained function.
	"""
	
	homepage = "https://github.com/jsugarelli/xplain/"
	cran = "xplain" 

	version("0.2.2", md5="7d820f0c9378242acb7727bfc8de4a35")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
