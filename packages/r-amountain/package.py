# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmountain(RPackage):
	"""Active modules for multilayer weighted gene co-expression networks: a continuous optimization approach

	A pure data-driven gene network, weighted gene co-expression network (WGCN) could be constructed only from expression profile. Different layers in such networks may represent different time points, multiple conditions or various species. AMOUNTAIN aims to search active modules in multi-layer WGCN using a continuous optimization approach.
	"""
	
	bioc = "AMOUNTAIN"

	version("1.34.0", commit="281214becf0a554984df5aa252de5c17ff93f887")
	version("1.28.0", commit="5f18a6da72f883ff71c174b4b4d0abd3357683e2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
