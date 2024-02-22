# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInflation(RPackage):
	"""Core Inflation

	Provides access to core inflation functions. Four different core inflation 
 functions are provided. The well known trimmed means, exclusion and double weighing methods, 
 alongside the new Triple Filter method introduced in Ferreira et al. (2016) <https://goo.gl/UYLhcj>.
	"""
	
	homepage = "https://github.com/fernote7/Inflation"
	cran = "Inflation" 

	version("0.1.0", md5="591cac9c4990355574fe5fb3924f1a7c")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
