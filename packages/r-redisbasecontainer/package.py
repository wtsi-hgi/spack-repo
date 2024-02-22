# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedisbasecontainer(RPackage):
	"""The Container for the DockerParallel Package

	
  Providing the container for the DockerParallel package.
	"""
	
	cran = "RedisBaseContainer" 

	version("1.0.1", md5="aa59d36b1076f10b4f6651aa1b2ac9cc")

	depends_on("r-dockerparallel@1.0.3:", type=("build", "run"))
