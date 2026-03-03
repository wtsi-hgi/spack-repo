# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemss(RPackage):
	"""Data Sets from Mixed-Effects Models in S

	Data sets and sample analyses from Pinheiro and Bates,
  "Mixed-effects Models in S and S-PLUS" (Springer, 2000).
	"""
	
	cran = "MEMSS" 

	version("0.9-3", md5="55f2b020443d598ece4ad09e07d5ee25")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-lme4@0.999375.36:", type=("build", "run"))
