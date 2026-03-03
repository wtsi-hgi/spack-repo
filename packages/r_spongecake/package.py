# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpongecake(RPackage):
	"""Transform a Movie into a Synthetic Picture

	Transform a Movie into a Synthetic Picture. A frame every 10 seconds is summarized into one colour, then every generated colors are stacked together.
	"""
	
	homepage = "https://github.com/ThinkRstat/spongecake"
	cran = "spongecake" 

	version("0.1.2", md5="2390c9b3abdae93885b040667f56ce5c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
