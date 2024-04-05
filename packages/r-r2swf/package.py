# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2swf(RPackage):
	"""Convert R Graphics to Flash Animations

	Using the 'Ming' library
    <https://github.com/libming/libming> to create Flash animations.
    Users can either use the 'SWF' device swf() to generate 'SWF' file
    directly through plotting functions like plot() and lines(),
    or convert images of other formats ('SVG', 'PNG', 'JPEG') into 'SWF'.
	"""
	
	homepage = "https://github.com/yixuan/R2SWF"
	cran = "R2SWF" 

	version("0.9-9", md5="f478de254a18e3e53cfd33dd3fb1acb5")
	version("0.9-8", md5="b3172e129b04d250657b8da4392f6b34")

	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("freetype", type=("build", "link", "run"))
