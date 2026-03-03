# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColourvalues(RPackage):
	"""Assigns Colours to Values

	Maps one of the viridis colour palettes, or a user-specified palette to values. 
    Viridis colour maps are created by Stéfan van der Walt and Nathaniel Smith, 
    and were set as the default palette for the 'Python' 'Matplotlib' library <https://matplotlib.org/>. 
    Other palettes available in this library have been derived from 
    'RColorBrewer' <https://CRAN.R-project.org/package=RColorBrewer> and 
    'colorspace' <https://CRAN.R-project.org/package=colorspace> packages.
	"""
	
	homepage = "https://symbolixau.github.io/colourvalues/"
	cran = "colourvalues" 

	version("0.3.9", md5="6fafd9e1e0234875b6744ef786f62160")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-bh@1.81:", type=("build", "run"))
