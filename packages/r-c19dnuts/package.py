# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC19dnuts(RPackage):
	"""Dataset of Regional COVID-19 Deaths per 100,000 Pop (NUTS)

	Dataset containing cumulative COVID-19 deaths (absolute and per 100,000 pop) at the regional level (mostly NUTS 3) for 31 EU/EFTA countries.
	"""
	
	cran = "C19dNUTS" 

	version("1.0.1", md5="41f16a15cb01358c5d401d2069890bbe")

	depends_on("r@3.5:", type=("build", "run"))
