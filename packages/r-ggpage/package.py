# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpage(RPackage):
	"""Creates Page Layout Visualizations

	Facilitates the creation of page layout
    visualizations in which words are represented as rectangles with sizes
    relating to the length of the words. Which then is divided in lines
    and pages for easy overview of up to quite large texts.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/ggpage"
	cran = "ggpage" 

	version("0.2.3", md5="487ba98d0df0b51fe72e15bb04a25af3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidytext@0.1:", type=("build", "run"))
