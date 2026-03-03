# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrightmap(RPackage):
	"""IRT Item-Person Map with 'ConQuest' Integration

	A powerful yet simple graphical tool available in the field of psychometrics is the Wright Map (also known as item maps or item-person maps), which presents the location of both respondents and items on the same scale. Wright Maps are commonly used to present the results of dichotomous or polytomous item response models. The 'WrightMap' package provides functions to create these plots from item parameters and person estimates stored as R objects. Although the package can be used in conjunction with any software used to estimate the IRT model (e.g. 'TAM', 'mirt', 'eRm' or 'IRToys' in 'R', or 'Stata', 'Mplus', etc.),  'WrightMap' features special integration with 'ConQuest' to facilitate reading and plotting its output directly.The 'wrightMap' function creates Wright Maps based on person estimates and item parameters produced by an item response analysis. The 'CQmodel' function reads output files created using 'ConQuest' software and creates a set of data frames for easy data manipulation, bundled in a 'CQmodel' object. The 'wrightMap' function can take a 'CQmodel' object as input or it can be used to create Wright Maps directly from data frames of person and item parameters.
	"""
	
	cran = "WrightMap" 

	version("1.3", md5="ded7310ae2971c7eca3c93c9db408811")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
