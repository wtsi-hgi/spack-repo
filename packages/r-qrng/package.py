# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrng(RPackage):
	"""(Randomized) Quasi-Random Number Generators

	Functionality for generating (randomized) quasi-random numbers in
  high dimensions.
	"""
	
	cran = "qrng" 

	version("0.0-10", md5="513e4f9ab2775a64941dd45b943deea5")

	depends_on("r@3:", type=("build", "run"))
