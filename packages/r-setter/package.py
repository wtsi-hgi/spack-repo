# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetter(RPackage):
	"""Mutators that Work with Pipes

	Mutators to set attributes of variables, that work well in a pipe
    (much like stats::setNames()).
	"""
	
	homepage = "https://bitbucket.org/richierocks/setter"
	cran = "setter" 

	version("0.0-1", md5="99d7e50ff664e56e5f2adabe0114c69d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.5:", type=("build", "run"))
