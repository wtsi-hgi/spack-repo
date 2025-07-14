# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAll(RPackage):
	"""A data package

	Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz Laboratory at the DFCI (includes Apr 2004 versions)
	"""
	
	bioc = "ALL"

	version("1.50.0", commit="81e0f2f7343c963c2fd37fb65216d8bddad5464a")
	version("1.44.0", commit="443566ea4db2dfdd11ff7e9928a3b6a03c12e326")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

