# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrsnls(RPackage):
	"""Nonlinear Regression Parameters Estimation by 'CRS4HC' and
'CRS4HCe'

	Functions for nonlinear regression parameters estimation by algorithms based on Controlled Random Search algorithm.
  Both functions (crs4hc(), crs4hce()) adapt current search strategy by four heuristics competition. In addition, crs4hce() improves adaptability by adaptive stopping condition.
	"""
	
	cran = "crsnls" 

	version("0.2", md5="e8a464288b62c9568ca3a1166dc7ea26")

