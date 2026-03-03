# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmhnpa(RPackage):
	"""Cochran-Mantel-Haenszel and Nonparametric ANOVA

	Cochran-Mantel-Haenszel methods (Cochran (1954) <doi:10.2307/3001616>; Mantel and Haenszel (1959) <doi:10.1093/jnci/22.4.719>; Landis et al. (1978) <doi:10.2307/1402373>) are a suite of tests applicable to categorical data. A competitor to those tests is the procedure of Nonparametric ANOVA which was initially introduced in Rayner and Best (2013) <doi:10.1111/anzs.12041>. The methodology was then extended in Rayner et al. (2015) <doi:10.1111/anzs.12113>. This package employs functions related to both methodologies and serves as an accompaniment to the book: An Introduction to Cochran–Mantel–Haenszel and Non-Parametric ANOVA. The package also contains the data sets used in that text.
	"""
	
	cran = "CMHNPA" 

	version("1.1.1", md5="d589ed0c65f8ba8f832ae47f839ccd45")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
