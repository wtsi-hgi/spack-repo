# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmvanova(RPackage):
	"""Novice Model Variation ANOVA

	Due to 'Rstudio's' status as open source software, we believe it will be utilized frequently for future data analysis by users whom lack formal training or experience with 'R'. The 'NMVANOVA' (Novice Model Variation ANOVA) a streamlined variation of experimental design functions that allows novice 'Rstudio' users to perform different model variations one-way analysis of variance without downloading  multiple libraries or packages. Users can easily manipulate the data block, and needed inputs so that users only have to plugin the four designed variables/values.
	"""
	
	cran = "NMVANOVA" 

	version("1.1.0", md5="eda967939b2759b3e42b6077dbb191fa")

