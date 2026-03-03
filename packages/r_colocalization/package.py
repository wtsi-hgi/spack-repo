# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColocalization(RPackage):
	"""Normalized Spatial Intensity Correlation

	Calculate the colocalization index, NSInC, in two different ways as described in the paper (Liu et al., 2019. Manuscript submitted for publication.) for multiple-species spatial data which contain the precise locations and membership of each spatial point. The two main functions are nsinc.d() and nsinc.z(). They provide the Pearson’s correlation coefficients of signal proportions in different memberships within a concerned proximity of every signal (or every base signal if single direction colocalization is considered) across all (base) signals using two different ways of normalization. The proximity sizes could be an individual value or a range of values, where the default ranges of values are different for the two functions.
	"""
	
	cran = "colocalization" 

	version("1.0.2", md5="fcd8a8ff09d4b006ccdba031853873c1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
