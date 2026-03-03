# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaebest(RPackage):
	"""Selecting Auxiliary Variables in Small Area Estimation (SAE)
Model

	Select best combination of auxiliary variables with certain criterion.
	"""
	
	cran = "saeBest" 

	version("0.1.0", md5="cc3bacc68119dc6d4032cb5c01a00c7d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sae", type=("build", "run"))
