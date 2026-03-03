# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMasstimate(RPackage):
	"""Body Mass Estimation Equations for Vertebrates

	Estimation equations are from a variety of sources and associated error estimation.
	"""
	
	cran = "MASSTIMATE" 

	version("2.0-1", md5="89691427c24ecb452eb0ee9fd4ec6f9f")

	depends_on("r@3.5:", type=("build", "run"))
