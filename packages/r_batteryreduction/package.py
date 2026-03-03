# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatteryreduction(RPackage):
	"""An R Package for Data Reduction by Battery Reduction

	Battery reduction is a method used in data reduction. It uses Gram-Schmidt orthogonal rotations to find out a subset of variables best representing the original set of variables.    
	"""
	
	cran = "batteryreduction" 

	version("0.1.1", md5="9ce6abc2cb14b4fb5e938a60f5c2f2c8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
