# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcolors(RPackage):
	"""Color Mappings and 'C++' Header Files for Color Conversion

	Provides 'C++' header files to deal with color conversion
    from some color spaces to hexadecimal with 'Rcpp', and exports some
    color mapping functions for usage in R. Also exports functions to
    convert colors from the 'HSLuv' color space for usage in R. 'HSLuv' is
    a human-friendly alternative to HSL.
	"""
	
	homepage = "https://github.com/stla/RcppColors"
	cran = "RcppColors" 

	version("0.6.0", md5="ef46ea80fa51f788e17b7fe812baead6")

	depends_on("r-rcpp", type=("build", "run"))
