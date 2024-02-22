# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisvow(RPackage):
	"""Visible Vowels: Visualization of Vowel Variation

	Visualizes vowel variation in f0, F1, F2, F3 and duration.
	"""
	
	homepage = "https://www.visiblevowels.org/"
	cran = "visvow" 

	version("1.3.11", md5="89676af14467af186a1258f7e423d7cd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pbsmapping", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-effectsize", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-tikzdevice", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
