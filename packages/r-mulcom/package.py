# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulcom(RPackage):
	"""Calculates Mulcom test

	Identification of differentially expressed genes and false discovery rate (FDR) calculation by Multiple Comparison test.
	"""
	
	bioc = "Mulcom"

	version("1.58.0", commit="ffdd56f5c4e3416e523335f8739634770447aa8a")
	version("1.52.0", commit="3a9c5e5bdd3043bca94526e13681aa00847188a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
