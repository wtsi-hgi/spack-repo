# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgimage(RPackage):
	"""Use Image in 'ggplot2'

	Supports image files and graphic objects to be visualized in
    'ggplot2' graphic system.
	"""
	
	homepage = "https://github.com/GuangchuangYu/ggimage"
	cran = "ggimage" 

	version("0.3.3", md5="8885f142e42910a64e8b8906cb8dd3a9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfun", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
