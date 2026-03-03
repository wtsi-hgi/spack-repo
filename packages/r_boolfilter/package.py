# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoolfilter(RPackage):
	"""Optimal Estimation of Partially Observed Boolean Dynamical
Systems

	Tools for optimal and approximate state estimation as well as
    network inference of Partially-Observed Boolean Dynamical Systems.
	"""
	
	cran = "BoolFilter" 

	version("1.0.0", md5="984af85b942a9e97ec25ac17be2ce100")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rlab", type=("build", "run"))
	depends_on("r-boolnet", type=("build", "run"))
