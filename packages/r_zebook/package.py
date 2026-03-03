# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebook(RPackage):
	"""Working with Dynamic Models for Agriculture and Environment

	R package accompanying the book Working with dynamic models for agriculture and environment, by Daniel Wallach (INRA), David Makowski (INRA), James W. Jones (U.of Florida), Francois Brun (ACTA). 3rd edition 2018-09-27.
	"""
	
	cran = "ZeBook" 

	version("1.1", md5="cd505d079c7dfc7a43bcb75d31d606d0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
