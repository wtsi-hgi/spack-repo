# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMexbrewer(RPackage):
	"""Color Palettes Inspired by Works of Mexican Painters and
Muralists

	Color palettes inspired by the works of 
  Mexican painters and muralists. The package includes functions that
  return vectors of colors and also functions to use color and fill
  scales in 'ggplot2' visualizations.
	"""
	
	homepage = "https://github.com/paezha/MexBrewer"
	cran = "MexBrewer" 

	version("0.0.2", md5="ccd3141aae06e16dfca82b1d6c20d776")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
