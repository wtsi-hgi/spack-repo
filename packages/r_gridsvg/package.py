# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridsvg(RPackage):
	"""Export 'grid' Graphics as SVG

	Functions to export graphics drawn with package grid to SVG
  format.  Additional functions provide access to SVG features that
  are not available in standard R graphics, such as hyperlinks, 
  animation, filters, masks, clipping paths, and gradient and pattern fills.
	"""
	
	cran = "gridSVG" 

	version("1.7-5", md5="49c9794b0600ad93903751eb9c6f5534")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
