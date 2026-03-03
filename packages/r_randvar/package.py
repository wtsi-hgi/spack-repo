# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandvar(RPackage):
	"""Implementation of Random Variables

	Implements random variables by means of S4 classes and methods.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/robast/"
	cran = "RandVar" 

	version("1.2.3", md5="28b6695235e1e8684d1b1c212314cd31")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
