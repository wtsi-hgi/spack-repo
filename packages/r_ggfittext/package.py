# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfittext(RPackage):
	"""Fit Text Inside a Box in 'ggplot2'

	A 'ggplot2' extension to fit text into a box by growing, shrinking or wrapping the text.
	"""
	
	homepage = "https://wilkox.org/ggfittext/"
	cran = "ggfittext" 

	version("0.10.2", md5="1a004ab4a3be0fbd117491188fa467f2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-stringi@1.1.2:", type=("build", "run"))
	depends_on("r-shades@1.3.1:", type=("build", "run"))
	depends_on("r-gridtext@0.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
