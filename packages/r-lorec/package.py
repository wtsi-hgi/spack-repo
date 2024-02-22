# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorec(RPackage):
	"""LOw Rand and sparsE Covariance matrix estimation

	Estimate covariance matrices that contain low rank and sparse components
	"""
	
	cran = "lorec" 

	version("0.6.1", md5="21d2945ed160db5033c5225c44aa90f0")

