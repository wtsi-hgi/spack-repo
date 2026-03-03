# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmi(RPackage):
	"""Checks for Various Computing Environments

	A collection of lightweight functions that can be
    used to determine the computing environment in which your code is
    running. This includes operating systems, continuous integration (CI)
    environments, containers, and more.
	"""
	
	homepage = "https://github.com/briandconnelly/ami"
	cran = "ami" 

	version("0.1.0", md5="db4ee94f3dd5f01d1e69f6d52b657b66")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
