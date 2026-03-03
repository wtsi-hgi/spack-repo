# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfig(RPackage):
	"""Manage Environment Specific Configuration Values

	Manage configuration values across multiple environments (e.g.
  development, test, production). Read values using a function that determines
  the current environment and returns the appropriate value.
	"""
	
	homepage = "https://rstudio.github.io/config/"
	cran = "config" 

	version("0.3.2", md5="b476973a136c5c5d335103d6cd4dbb58")

	depends_on("r-yaml@2.1.19:", type=("build", "run"))
