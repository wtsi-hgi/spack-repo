# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghilbertstrings(RPackage):
	"""A Fast 'ggplot2'-Based Implementation of Hilbert Curves

	A set of functions that help to create plots based on Hilbert curves. 
    Hilbert curves are used to map one dimensional data into the 2D plane.
    The package provides a function that generate a 2D coordinate from an 
    integer position. As a specific use case the package provides a function 
    that allows mapping a character column in a data frame into 2D space 
    using 'ggplot2'. This allows visually comparing long lists of URLs, words,
    genes or other data that has a fixed order and position.
	"""
	
	homepage = "https://github.com/Sumidu/gghilbertstrings"
	cran = "gghilbertstrings" 

	version("0.3.3", md5="9fb9c0ed2c4946dc7ee86cfb3b4a8df1")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
