# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColocr(RPackage):
	"""Conduct Co-Localization Analysis of Fluorescence Microscopy
Images

	Automate the co-localization analysis of fluorescence microscopy 
  images. Selecting regions of interest, extract pixel intensities from 
  the image channels and calculate different co-localization statistics. The
  methods implemented in this package are based on Dunn et al. (2011) 
  <doi:10.1152/ajpcell.00462.2010>.
	"""
	
	homepage = "https://docs.ropensci.org/colocr"
	cran = "colocr" 

	version("0.1.1", md5="9bb56347377c055c7ec083fd259d364b")

	depends_on("r-imager", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
