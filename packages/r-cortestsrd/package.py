# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCortestsrd(RPackage):
	"""Significance Testing of Rank Cross-Correlations under SRD

	Significance test of Spearman's Rho or Kendall's Tau 
             between short-range dependent random variables.
	"""
	
	cran = "corTESTsrd" 

	version("1.0-0", md5="9cc01ad3996aa0e40a38ce641dd8e70c")

	depends_on("r@3.5:", type=("build", "run"))
