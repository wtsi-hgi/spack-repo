# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPumilior(RPackage):
	"""Pumilio in R

	R package to query and get data out of a Pumilio sound archive system (http://ljvillanueva.github.io/pumilio/).
	"""
	
	homepage = "http://ljvillanueva.github.io/pumilioR/"
	cran = "pumilioR" 

	version("1.3.1", md5="89257bf2a7b6c259f01db44b1100213b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
