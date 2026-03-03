# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivator(RPackage):
	"""A Multivariate Emulator

	A multivariate generalization of the emulator package.
	"""
	
	homepage = "https://github.com/RobinHankin/multivator"
	cran = "multivator" 

	version("1.1-11", md5="7510b8dd932e3a89523ad47afa7ef45b")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-emulator@1.2.15:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
