# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcamixdata(RPackage):
	"""Multivariate Analysis of Mixed Data

	Implements principal component analysis, orthogonal rotation and multiple
    factor analysis for a mixture of quantitative and qualitative variables.
	"""
	
	cran = "PCAmixdata" 

	version("3.1", md5="71277d8856c757345a6ede5971c2bdfe")

