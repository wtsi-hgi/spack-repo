# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsotonicPen(RPackage):
	"""Penalized Isotonic Regression in one and two dimensions

	Given a response y and a one- or two-dimensional predictor, the isotonic regression estimator is calculated with the usual orderings.  
	"""
	
	cran = "isotonic.pen" 

	version("1.0", md5="5ca89901dacbadc59e3cde84700bede9")

	depends_on("r-coneproj", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
