# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmbinning(RPackage):
	"""Scoring Modeling and Optimal Binning

	A set of functions to build a scoring model from beginning to end, leading the user
	to follow an efficient and organized development process, reducing significantly the time
	spent on data exploration, variable selection, feature engineering, binning and model selection 
	among other recurrent tasks. 
	The package also incorporates monotonic and customized binning, scaling capabilities that 
	transforms logistic coefficients into points for a better business understanding and 
	calculates and visualizes classic performance metrics of a classification model.
	"""
	
	cran = "smbinning" 

	version("0.9", md5="59474ca5148bb47630353c785b5e45ac")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
