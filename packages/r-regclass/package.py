# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegclass(RPackage):
	"""Tools for an Introductory Class in Regression and Modeling

	Contains basic tools for visualizing, interpreting, and building regression models.  It has been designed for use with the book Introduction to Regression and Modeling with R by Adam Petrie, Cognella Publishers, ISBN: 978-1-63189-250-9 <https://titles.cognella.com/introduction-to-regression-and-modeling-with-r-9781631892509>.
	"""
	
	cran = "regclass" 

	version("1.6", md5="08dda711ce9364e8650c0e073a140fff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bestglm", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
