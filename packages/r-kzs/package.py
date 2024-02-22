# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKzs(RPackage):
	"""Kolmogorov-Zurbenko Spatial Smoothing and Applications

	A spatial smoothing algorithm based on convolutions of finite rectangular kernels that provides sharp resolution in the presence of high levels of noise.
	"""
	
	cran = "kzs" 

	version("1.4", md5="eabab20e7d34d1cde5eed381e97458ca")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
