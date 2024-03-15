# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBallmapper(RPackage):
	"""The Ball Mapper Algorithm

	The core algorithm is described in "Ball mapper: a shape summary for topological data analysis" by Pawel Dlotko, (2019) <arXiv:1901.07410>. Please consult the following youtube video <https://www.youtube.com/watch?v=M9Dm1nl_zSQfor> the idea of functionality. Ball Mapper provide a topologically accurate summary of a data in a form of an abstract graph. To create it, please provide the coordinates of points (in the points array), values of a function of interest at those points (can be initialized randomly if you do not have it) and the value epsilon which is the radius of the ball in the Ball Mapper construction. It can be understood as the minimal resolution on which we use to create the model of the data. 
	"""
	
	cran = "BallMapper" 

	version("0.2.0", md5="1e0edf6ceac027472f413243a74df056")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
