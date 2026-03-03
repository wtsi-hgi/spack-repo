# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViscollin(RPackage):
	"""Visualizing Collinearity Diagnostics

	Provides methods to calculate diagnostics for multicollinearity among predictors in a linear or
  generalized linear model. It also provides methods to visualize those diagnostics following Friendly & Kwan (2009),
  "Where’s Waldo: Visualizing Collinearity Diagnostics", <doi:10.1198/tast.2009.0012>.
  These include better tabular presentation of collinearity diagnostics that highlight the important numbers,
  a semi-graphic tableplot of the diagnostics to make warning and danger levels more salient,
  and a "collinearity biplot" of the smallest dimensions of predictor space, where collinearity is most apparent. 
	"""
	
	homepage = "https://github.com/friendly/VisCollin"
	cran = "VisCollin" 

	version("0.1.2", md5="847b4960b8d5fdbb7fe366e4e89534f7")

	depends_on("r@3.5:", type=("build", "run"))
