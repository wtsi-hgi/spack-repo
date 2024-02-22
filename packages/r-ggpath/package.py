# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpath(RPackage):
	"""Robust Image Rendering Support for 'ggplot2'

	A 'ggplot2' extension that enables robust image grobs in
    panels and theme elements.
	"""
	
	homepage = "https://github.com/mrcaseb/ggpath"
	cran = "ggpath" 

	version("1.0.1", md5="62ed3a423310849aa2cffceee1bc6ad0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cachem@1:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magick@2.7.3:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
