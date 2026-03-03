# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtern(RPackage):
	"""A Ternary Conditional Operator for R

	A small language extension for succinct conditional assignment using `?` and `:`, emulating the conditional ternary operator syntax using in C, Java, JavaScript and other languages.
	"""
	
	homepage = "https://github.com/grddavies/rtern"
	cran = "rtern" 

	version("0.1.2", md5="5ba3dd3be30cfd159c5b7f3e03cb422e")

	depends_on("r-rlang", type=("build", "run"))
