# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHexsticker(RPackage):
	"""Create Hexagon Sticker in R

	Helper functions for creating reproducible hexagon sticker purely in R.
	"""
	
	homepage = "https://github.com/GuangchuangYu/hexSticker"
	cran = "hexSticker" 

	version("0.4.9", md5="fa0bbb5f113a19d51153756e9aefa4b6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
