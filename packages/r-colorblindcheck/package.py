# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorblindcheck(RPackage):
	"""Check Color Palettes for Problems with Color Vision Deficiency

	Compare color palettes with simulations of color vision deficiencies - deuteranopia, protanopia, and tritanopia.
        It includes calculation of distances between colors, and creating summaries of differences between a color palette and simulations of color vision deficiencies.
        This work was inspired by the blog post at <http://www.vis4.net/blog/2018/02/automate-colorblind-checking/>.
	"""
	
	homepage = "https://jakubnowosad.com/colorblindcheck/"
	cran = "colorblindcheck" 

	version("1.0.2", md5="3c4b964e53622b1288e98c1788461f9d")

	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-spacesxyz", type=("build", "run"))
