# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSysfonts(RPackage):
	"""Loading Fonts into R

	Loading system fonts and Google Fonts
    <https://fonts.google.com/> into R, in order to
    support other packages such as 'R2SWF' and 'showtext'.
	"""
	
	homepage = "https://github.com/yixuan/sysfonts"
	cran = "sysfonts" 

	version("0.8.9", md5="c5a568cf3ee93e7050592369d5f32165")

	depends_on("zlib", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("freetype", type=("build", "link", "run"))
