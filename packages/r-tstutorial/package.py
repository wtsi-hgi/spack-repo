# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTstutorial(RPackage):
	"""Fitting and Predict Time Series Interactive Laboratory

	Interactive laboratory of Time Series based in Box-Jenkins methodology.
	"""
	
	cran = "TSTutorial" 

	version("1.2.7", md5="b64390fc2800b033cb7af9bf6d074ef8")

	depends_on("r-mass", type=("build", "run"))
