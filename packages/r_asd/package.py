# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsd(RPackage):
	"""Simulations for Adaptive Seamless Designs

	Package runs simulations for adaptive seamless designs with and without early outcomes 
                           for treatment selection and subpopulation type designs.
	"""
	
	cran = "asd" 

	version("2.2", md5="8f073fe0c2c71e8892d4ef1f6ec81fa4")

	depends_on("r-mvtnorm", type=("build", "run"))
