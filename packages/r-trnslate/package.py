# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrnslate(RPackage):
	"""Translate R Code in Source Files

	Evaluate inline or chunks of R code in template files and replace with their output modifying the resulting template.
	"""
	
	homepage = "<https://marioma.me?i=soft>"
	cran = "tRnslate" 

	version("0.0.3", md5="43d0aee4a349593f0351a1c13f9aa22a")

	depends_on("r@2.10:", type=("build", "run"))
