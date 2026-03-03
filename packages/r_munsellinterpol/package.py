# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMunsellinterpol(RPackage):
	"""Interpolate Munsell Renotation Data from Hue/Chroma to CIE/RGB

	Methods for interpolating data in the Munsell color system following the ASTM D-1535 standard. Hues and chromas with decimal values can be interpolated and converted to/from the Munsell color system and CIE xyY, CIE XYZ, CIE Lab, CIE Luv, or RGB.  Includes ISCC-NBS color block lookup.  Based on the work by Paul Centore, "The Munsell and Kubelka-Munk Toolbox".
	"""
	
	cran = "munsellinterpol" 

	version("3.0-0", md5="16e7e79e0c6deabcefd0f43d8827c1b6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-spacesrgb", type=("build", "run"))
	depends_on("r-spacesxyz", type=("build", "run"))
