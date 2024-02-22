# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGipfrm(RPackage):
	"""Generalized Iterative Proportional Fitting for Relational Models

	Maximum likelihood estimation under relational models, with or without the overall effect.
	"""
	
	cran = "gIPFrm" 

	version("3.1", md5="6211a3a537cd3550bff25ef76fc15de6")

