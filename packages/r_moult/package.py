# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoult(RPackage):
	"""Models for Analysing Moult in Birds

	Functions to estimate start and duration of moult from moult 
             data, based on models developed in Underhill 
             and Zucchini (1988, 1990). 
	"""
	
	cran = "moult" 

	version("2.3.1", md5="3e712e48abdd3a5a3a9dee5a2fbcf3f3")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
