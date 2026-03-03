# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStuart(RPackage):
	"""Subtests Using Algorithmic Rummaging Techniques

	Construct subtests from a pool of items by using ant-colony-optimization, genetic algorithms, brute force, or random sampling.
  Schultze (2017) <doi:10.17169/refubium-622>.
	"""
	
	cran = "stuart" 

	version("0.10.2", md5="c95f99dc42ecde23da178d017458d993")

	depends_on("r@4.1:", type=("build", "run"))
