# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspi(RPackage):
	"""Analysis of Symmetry of Parasitic Infections

	Tools for the analysis and visualization of bilateral asymmetry in parasitic infections.
	"""
	
	cran = "aspi" 

	version("0.2.0", md5="332a6da72dc3463fb99acd21b7313252")

	depends_on("r@2.10:", type=("build", "run"))
