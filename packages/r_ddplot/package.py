# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdplot(RPackage):
	"""Create D3 Based SVG Graphics

	Create 'D3' based 'SVG' ('Scalable Vector Graphics') graphics using a simple 'R' API. 
    The package aims to simplify
    the creation of many 'SVG' plot types using a straightforward 'R' API.  
    The package relies on the 'r2d3' 'R' package and the 'D3' 'JavaScript' library. 
    See <https://rstudio.github.io/r2d3/> and <https://d3js.org/> respectively.
	"""
	
	homepage = "https://github.com/feddelegrand7/ddplot"
	cran = "ddplot" 

	version("0.0.1", md5="cd7320ad59a9e502aa314c60d0d17775")

	depends_on("r-r2d3", type=("build", "run"))
