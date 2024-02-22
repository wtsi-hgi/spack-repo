# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyemoji(RPackage):
	"""Discovers Emoji from Text

	Unicodes are not friendly to work with, and not all Unicodes are
    Emoji per se, making obtaining Emoji statistics a difficult task. This
    tool can help your experience of working with Emoji as smooth as possible,
    as it has the 'tidyverse' style. 
	"""
	
	homepage = "https://pursuitofdatascience.github.io/tidyEmoji/"
	cran = "tidyEmoji" 

	version("0.1.1", md5="0d2b81ab0bba5a273b8c4adda7c1c3dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emoji", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
