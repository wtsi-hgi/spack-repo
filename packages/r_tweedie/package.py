# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweedie(RPackage):
	"""Evaluation of Tweedie Exponential Family Models

	Maximum likelihood computations for Tweedie families, including the series expansion (Dunn and Smyth, 2005; <doi:10.1007/s11222-005-4070-y>) and the Fourier inversion  (Dunn and Smyth, 2008; <doi:10.1007/s11222-007-9039-6>), and related methods.
	"""
	
	cran = "tweedie" 

	version("2.3.5", md5="b4048e492744c22b39c9ca631e1c1b81")

	depends_on("r@2.8:", type=("build", "run"))
