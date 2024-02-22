# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPstat(RPackage):
	"""Assessing Pst Statistics

	Calculating Pst values to assess differentiation among populations from a set of quantitative traits is the primary purpose of such a package. The bootstrap method provides confidence intervals and distribution histograms of Pst. Variations of Pst in function of the parameter c/h^2 are studied as well. Finally, the package proposes different transformations especially to eliminate any variation resulting from allometric growth (calculation of residuals from linear regressions, Reist standardizations or Aitchison transformation).
	"""
	
	cran = "Pstat" 

	version("1.2", md5="8ecd1d1f3ffa0865b14a97a1e8009b1d")

