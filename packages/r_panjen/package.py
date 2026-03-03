# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanjen(RPackage):
	"""A Semi-Parametric Test for Specifying Functional Form

	A central decision in a parametric regression is how to specify the relation between an dependent variable and each explanatory variable. This package provides a semi-parametric tool for comparing different transformations of an  explanatory variables in a parametric regression. The functions is relevant in a situation, where you would use a box-cox or Box-Tidwell transformations.  In contrast to the classic power-transformations, the methods in this package allows for  theoretical driven user input and the possibility to compare with a non-parametric transformation.
	"""
	
	cran = "PanJen" 

	version("1.6", md5="4f055e97df7ee1b177a14f4bca845167")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
