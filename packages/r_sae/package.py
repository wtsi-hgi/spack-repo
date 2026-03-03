# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSae(RPackage):
	"""Small Area Estimation

	Functions for small area estimation.
	"""
	
	cran = "sae" 

	version("1.3", md5="76289a4e9789f02cb39f8d5abc6e5e72")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
