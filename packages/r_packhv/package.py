# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackhv(RPackage):
	"""A few Useful Functions for Statisticians

	Various useful functions for statisticians: describe data, plot Kaplan-Meier curves with numbers of subjects at risk, compare data sets, display spaghetti-plot, build multi-contingency tables...
	"""
	
	cran = "packHV" 

	version("2.2", md5="c37fa44e2a5057492e6f0f7b20a84cca")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-writexls@2.3:", type=("build", "run"))
