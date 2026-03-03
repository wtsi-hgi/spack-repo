# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbounds(RPackage):
	"""Perform Rosenbaum Bounds Sensitivity Tests for Matched and
Unmatched Data

	Takes matched and unmatched data and calculates Rosenbaum bounds for the treatment effect.  Calculates bounds for binary outcome data, Hodges-Lehmann point estimates, Wilcoxon signed-rank test for matched data and matched IV estimators, Wilcoxon sum rank test, and for data with multiple matched controls. The sensitivity analysis methods in this package are documented in Rosenbaum (2002) Observational Studies, <doi:10.1007/978-1-4757-3692-2>, Springer-Verlag.
	"""
	
	cran = "rbounds" 

	version("2.2", md5="7f84e0b104d1abb601713aab6a838687")

