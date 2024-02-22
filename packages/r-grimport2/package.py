# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrimport2(RPackage):
	"""Importing 'SVG' Graphics

	Functions for importing external vector images and
  drawing them as part of 'R' plots.  This package is different from the
  'grImport' package because, where that package imports 'PostScript'
  format images, this package imports 'SVG' format images.  Furthermore,
  this package imports a specific subset of 'SVG', so external images
  must be preprocessed using a package like 'rsvg' to produce 'SVG'
  that this package can import.  'SVG' features that are not supported
  by 'R' graphics, e.g., gradient fills, can be imported and then
  exported via the 'gridSVG' package.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/grimport/"
	cran = "grImport2" 

	version("0.3-1", md5="29f8f9c3278a8d81cece3ff853a3c797", url="https://cran.r-project.org/src/contrib/grImport2_0.3-1.tar.gz")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
