# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinycodet(RPackage):
	"""Functions to Help in your Coding Etiquette

	Adds some functions to help in your coding etiquette.
    'tinycodet' primarily focuses on 4 aspects.
    1) Safer decimal (in)equality testing, safer atomic conversions, and other functions for safer coding.
    2) A new package import system,
    that attempts to combine the benefits of using a package without attaching it,
    with the benefits of attaching a package.
    3) Extending the string manipulation capabilities of the 'stringi' R package.
    4) Reducing repetitive code.
    Besides linking to 'Rcpp', 'tinycodet' has only one other dependency, namely 'stringi'.
	"""
	
	homepage = "https://github.com/tony-aw/tinycodet/"
	cran = "tinycodet" 

	version("0.4.5", md5="cb1444dd415b1fa93c19b38319b13e6a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi@1.7.12:", type=("build", "run"))
