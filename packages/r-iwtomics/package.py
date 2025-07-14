# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIwtomics(RPackage):
	"""Interval-Wise Testing for Omics Data

	Implementation of the Interval-Wise Testing (IWT) for omics data. This inferential procedure tests for differences in "Omics" data between two groups of genomic regions (or between a group of genomic regions and a reference center of symmetry), and does not require fixing location and scale at the outset.
	"""
	
	bioc = "IWTomics"

	version("1.32.0", commit="e173d780a7bfd556fc14f7b5d699b76706fb0e24")
	version("1.26.0", commit="422b48d160fcd8076b70ff7923064fdc3dee49a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
