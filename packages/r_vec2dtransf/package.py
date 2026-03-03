# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVec2dtransf(RPackage):
	"""2D Cartesian Coordinate Transformation

	Applies affine and similarity transformations on vector spatial data (sp objects). Transformations can be defined from control points or directly from parameters. If redundant control points are provided Least Squares is applied allowing to obtain residuals and RMSE.
	"""
	
	homepage = "https://github.com/gacarrillor/vec2dtransf"
	cran = "vec2dtransf" 

	version("1.1.3", md5="b3ba6e77bf534b344b8957d740e7dc7e")

	depends_on("r-sp", type=("build", "run"))
