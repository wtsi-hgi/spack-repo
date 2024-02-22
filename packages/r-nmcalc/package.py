# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmcalc(RPackage):
	"""Basic Calculations for PK/PD Modeling

	Essentials for PK/PD (pharmacokinetics/pharmacodynamics) such as area under the curve, (geometric) coefficient of variation, and other calculations that are not part of base R. This is not a noncompartmental analysis (NCA) package.
	"""
	
	cran = "NMcalc" 

	version("0.0.3", md5="0de85f95fe1e9b7f958806f598ca01ae")

	depends_on("r-data-table", type=("build", "run"))
