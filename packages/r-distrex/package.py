# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrex(RPackage):
	"""Extensions of Package 'distr'

	Extends package 'distr' by functionals, distances, and conditional distributions.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrEx" 

	version("2.9.2", md5="c8e66137d834721254d0e6d5f0513051")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
