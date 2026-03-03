# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsokernel(RPackage):
	"""Isolation Kernel

	Implementation of Isolation kernel (Qin et al. (2019) <doi:10.1609/aaai.v33i01.33014755>).
	"""
	
	homepage = "https://github.com/zhuye88/isokernel"
	cran = "isokernel" 

	version("0.1.0", md5="1dc977b50853f8f466bb736aa529988b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rann@2.6.1:", type=("build", "run"))
	depends_on("r-matrix@1.3.4:", type=("build", "run"))
