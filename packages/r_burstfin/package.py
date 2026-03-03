# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBurstfin(RPackage):
	"""Burns Statistics Financial

	A suite of functions for finance, including the estimation
	of variance matrices via a statistical factor model or
	Ledoit-Wolf shrinkage.
	"""
	
	homepage = "https://www.burns-stat.com/"
	cran = "BurStFin" 

	version("1.3", md5="584f814e5ccaf64a0ed575c19c8fce4e")

