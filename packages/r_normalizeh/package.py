# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalizeh(RPackage):
	"""Normalize Hadamard Matrix

	Normalize a given Hadamard matrix. A Hadamard matrix is said to be normalized when its first row and first column entries are all 1, see Hedayat, A. and Wallis, W. D. (1978) "Hadamard matrices and their applications. The Annals of Statistics, 1184-1238." <doi:10.1214/aos/1176344370>.
	"""
	
	cran = "normalizeH" 

	version("1.0.0", md5="6246046447f8470191667c8f748152ee")

	depends_on("r@4.2:", type=("build", "run"))
