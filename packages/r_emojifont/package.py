# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmojifont(RPackage):
	"""Emoji and Font Awesome in Graphics

	An implementation of using emoji and fontawesome for using in both
    base and 'ggplot2' graphics.
	"""
	
	homepage = "https://github.com/GuangchuangYu/emojifont"
	cran = "emojifont" 

	version("0.5.5", md5="4161fd0eb2249b450b7ec43d7a12801c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proto", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
