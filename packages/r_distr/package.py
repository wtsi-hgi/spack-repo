# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistr(RPackage):
	"""Object Oriented Implementation of Distributions

	S4-classes and methods for distributions.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distr" 

	version("2.9.3", md5="516d41cdd753fb0a200d0122332ed9b8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
