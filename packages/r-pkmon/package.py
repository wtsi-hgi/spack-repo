# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkmon(RPackage):
	"""Least-Squares Estimator under k-Monotony Constraint for Discrete
Functions

	We implement two least-squares estimators under k-monotony constraint using a method based on the Support Reduction Algorithm from Groeneboom et al (2008) <DOI:10.1111/j.1467-9469.2007.00588.x>. The first one is a projection estimator on the set of k-monotone discrete functions. The second one is a projection on the set of k-monotone discrete probabilities. This package provides functions to generate samples from the spline basis from Lefevre and Loisel (2013) <DOI:10.1239/jap/1378401239>, and from mixtures of splines.
	"""
	
	cran = "pkmon" 

	version("1.1", md5="454a45fa8cf56e4ed1bc2c9f229191a2")

