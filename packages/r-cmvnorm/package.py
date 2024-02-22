# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmvnorm(RPackage):
	"""The Complex Multivariate Gaussian Distribution

	Various utilities for the complex multivariate Gaussian distribution and complex Gaussian processes.
	"""
	
	homepage = "https://github.com/RobinHankin/cmvnorm"
	cran = "cmvnorm" 

	version("1.0-7", md5="924bdbf22fc33f30a95a0daa16d22cf7")

	depends_on("r-emulator@1.2.21:", type=("build", "run"))
	depends_on("r-elliptic", type=("build", "run"))
