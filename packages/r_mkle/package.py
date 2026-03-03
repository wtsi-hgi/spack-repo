# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkle(RPackage):
	"""Maximum Kernel Likelihood Estimation

	Package for fast computation of the maximum kernel likelihood estimator (mkle).
	"""
	
	cran = "MKLE" 

	version("1.0.1", md5="ed2279902094bcda459ecfd26b787a5c")

