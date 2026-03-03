# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssthemes(RPackage):
	"""RSS Palettes and Themes

	Defines colour palettes and themes for Royal Statistical 
  Society (RSS) publications, including Significance magazine. Palettes and 
  themes are supported in both base R and 'ggplot2' graphics, and are intended 
  to be used by authors submitting to RSS publications.
	"""
	
	homepage = "https://github.com/nrennie/RSSthemes"
	cran = "RSSthemes" 

	version("1.0.0", md5="f1b3c279b039f07ef4ba2db1cc37ff6a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
