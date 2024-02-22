# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortion(RPackage):
	"""Extracting a Data Portion

	Provides a simple method to extract portions of a vector, matrix, or data.frame. 
    The relative portion size and the way the portion is selected can be chosen.
	"""
	
	homepage = "https://github.com/loelschlaeger/portion"
	cran = "portion" 

	version("0.1.0", md5="9f52dce62df09b02db6dad46c6c33e95")

