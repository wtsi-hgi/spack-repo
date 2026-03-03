# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChi(RPackage):
	"""The Chi Distribution

	Light weight implementation of the standard distribution 
  functions for the chi distribution, wrapping those for the chi-squared 
  distribution in the stats package.
	"""
	
	homepage = "https://github.com/dkahle/chi"
	cran = "chi" 

	version("0.1", md5="8af53740f8a05c43602e0d1a6771be38")

