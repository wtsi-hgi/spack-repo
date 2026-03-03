# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMittagleffler(RPackage):
	"""Mittag-Leffler Family of Distributions

	Implements the Mittag-Leffler function, distribution,
  random variate generation, and estimation. Based on the Laplace-Inversion
  algorithm by Garrappa, R. (2015) <doi:10.1137/140971191>.
	"""
	
	homepage = "https://strakaps.github.io/MittagLeffleR/"
	cran = "MittagLeffleR" 

	version("0.4.1", md5="6bb45dfb715a72416524233a1181d0a9")

	depends_on("r-stabledist", type=("build", "run"))
