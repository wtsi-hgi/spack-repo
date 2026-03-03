# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoublecone(RPackage):
	"""Test Against Parametric Regression Function

	Performs hypothesis tests concerning a regression function in a least-squares model, where the null is a parametric function, and the alternative is the union of large-dimensional convex polyhedral cones. See Bodhisattva Sen and Mary C Meyer (2016) <doi:10.1111/rssb.12178> for more details.
	"""
	
	cran = "DoubleCone" 

	version("1.1", md5="90c27979043ab3822ea18e340d547115")

	depends_on("r-coneproj@1.12:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
