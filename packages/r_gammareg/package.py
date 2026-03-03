# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGammareg(RPackage):
	"""Classic Gamma Regression: Joint Modeling of Mean and Shape
Parameters

	Performs Gamma regression, where both mean and shape parameters follows lineal regression structures. 
	"""
	
	cran = "Gammareg" 

	version("3.0.1", md5="70413109d18ca92bc1afb99986dee9f3")

	depends_on("r@4:", type=("build", "run"))
