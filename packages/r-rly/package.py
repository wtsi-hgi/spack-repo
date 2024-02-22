# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRly(RPackage):
	"""Tools to Create Formal Language Parser

	R implementation of the common parsing tools 'lex' and 'yacc'.
	"""
	
	homepage = "https://github.com/systemincloud/rly"
	cran = "rly" 

	version("1.7.4", md5="4d1f2f155341ec2668e0d3a3b74bd47d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
