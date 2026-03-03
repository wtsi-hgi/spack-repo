# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmfn(RPackage):
	"""Non-Negative Matrix Factorization

	Non-negative Matrix Factorization.
	"""
	
	cran = "NMFN" 

	version("2.0.1", md5="7ad13e6c639b422c81a87706415ca389")

