# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracer(RPackage):
	"""Slick Call Stacks

	Better looking call stacks after an error.
	"""
	
	homepage = "https://github.com/mangothecat/tracer#readme"
	cran = "tracer" 

	version("1.0.0", md5="63872d9be0178309f0e136906505e634")

	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-prettycode", type=("build", "run"))
