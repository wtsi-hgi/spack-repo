# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalize(RPackage):
	"""Centering and Scaling of Numeric Data

	Provides a simple method for centering and scaling of numeric data. 
    Certain columns or rows can be ignored when normalizing or be normalized jointly.
	"""
	
	homepage = "https://github.com/loelschlaeger/normalize"
	cran = "normalize" 

	version("0.1.0", md5="6b43e5eba142692f4d23a423946bbcf4")

