# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpen(RPackage):
	"""Covariance and Inverse Covariance Matrix Estimation Using Joint
Penalty

	A Joint PENalty Estimation of Covariance and Inverse Covariance Matrices.
	"""
	
	cran = "JPEN" 

	version("1.0", md5="8e73d9b184b71336a626bd289fa7527e")

	depends_on("r-mvtnorm@1.0.2:", type=("build", "run"))
