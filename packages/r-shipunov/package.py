# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShipunov(RPackage):
	"""Miscellaneous Functions from Alexey Shipunov

	A collection of functions for data manipulation, plotting and statistical computing,
 to use separately or with the book "Visual Statistics. Use R!":
 Shipunov (2020) <http://ashipunov.info/shipunov/software/r/r-en.htm>.
 Dr Alexey Shipunov died in December 2022.
 Most useful functions:
 Bclust(), Jclust() and BootA() which bootstrap hierarchical clustering;
 Recode() which does multiple recoding in a fast, simple and flexible way;
 Misclass() which outputs confusion matrix even if classes are not concerted;
 Overlap() which measures group separation on any projection;
 Biarrows() which converts any scatterplot into biplot;
 and Pleiad() which is fast and flexible correlogram.
	"""
	
	cran = "shipunov" 

	version("1.17.1", md5="0b862f12bb11dcf452b922b610147655")

	depends_on("r-pbsmapping", type=("build", "run"))
