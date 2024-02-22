# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelimp(RPackage):
	"""Relative Contribution of Effects in a Regression Model

	Functions to facilitate inference on the relative importance of predictors in a linear or generalized linear model, and a couple of useful Tcl/Tk widgets.
	"""
	
	homepage = "http://warwick.ac.uk/relimp"
	cran = "relimp" 

	version("1.0-5", md5="0ce1f03f9ec99b940941d708e505afd0")

	depends_on("r@2:", type=("build", "run"))
