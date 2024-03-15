# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemometrics(RPackage):
	"""Multivariate Statistical Analysis in Chemometrics.

	R companion to the book "Introduction to Multivariate Statistical Analysis
	in Chemometrics" written by K. Varmuza and P. Filzmoser (2009)."""

	cran = "chemometrics"

	license("GPL-3.0-or-later")

	version("1.4.4", md5="a6a53c4f945eca943d9a234b8c598aec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
