# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjade(RPackage):
	"""A Clean, Whitespace-Sensitive Template Language for Writing HTML

	Jade is a high performance template engine heavily influenced by
    Haml and implemented with JavaScript for node and browsers.
	"""
	
	homepage = "https://github.com/jeroen/rjade"
	cran = "rjade" 

	version("0.1.1", md5="b6eee3564f502fb0d4413bd3ed77e3f1")

	depends_on("r-v8@0.5:", type=("build", "run"))
