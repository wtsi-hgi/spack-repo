# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPysd2r(RPackage):
	"""API to 'Python' Library 'pysd'

	Using the R package 'reticulate', this package creates an interface to the 'pysd' toolset.
    The package provides an R interface to a number of 'pysd' functions, and can read files in
    'Vensim' 'mdl' format, and 'xmile' format. The resulting simulations are returned as a 'tibble', and from 
    that the results can be processed using 'dplyr' and 'ggplot2'. The package has been tested  using 'python3'.
	"""
	
	cran = "pysd2r" 

	version("0.1.0", md5="6334a33300fcc8f353e55fa62e599036")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
