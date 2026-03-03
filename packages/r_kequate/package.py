# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKequate(RPackage):
	"""The Kernel Method of Test Equating

	Implements the kernel method of test equating as defined in von Davier, A. A., Holland, P. W. and Thayer, D. T. (2004) <doi:10.1007/b97446> and Andersson, B. and Wiberg, M. (2017) <doi:10.1007/s11336-016-9528-7> using the CB, EG, SG, NEAT CE/PSE and NEC designs, supporting Gaussian, logistic and uniform kernels and unsmoothed and pre-smoothed input data.
	"""
	
	cran = "kequate" 

	version("1.6.4", md5="77e71c6aa8ccd019733106513a4bd657")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-equateirt", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
