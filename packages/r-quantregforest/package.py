# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantregforest(RPackage):
	"""Quantile Regression Forests

	Quantile Regression Forests is a tree-based ensemble
        method for estimation of conditional quantiles. It is
        particularly well suited for high-dimensional data. Predictor
        variables of mixed classes can be handled. The package is
        dependent on the package 'randomForest', written by Andy Liaw.
	"""
	
	homepage = "http://github.com/lorismichel/quantregForest"
	cran = "quantregForest" 

	version("1.3-7", md5="89835b2d3492f081bfa35661aab84f1e")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
