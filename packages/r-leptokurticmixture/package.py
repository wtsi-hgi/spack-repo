# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeptokurticmixture(RPackage):
	"""Implements Parsimonious Finite Mixtures of Multivariate
Elliptical Leptokurtic-Normals

	A way to fit Parsimonious Finite Mixtures of Multivariate Elliptical Leptokurtic-Normals. Two methods of estimation are implemented. 
	"""
	
	cran = "leptokurticMixture" 

	version("1.1", md5="7d8933f94350b2ca6548944a4e015348")

