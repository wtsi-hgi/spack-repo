# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMed(RPackage):
	"""Mediation by Tilted Balancing

	Nonparametric estimation and inference for natural direct and indirect effects by Chan, Imai, Yam and Zhang (2016) <arXiv:1601.03501>.
	"""
	
	cran = "MED" 

	version("0.1.0", md5="6dceb744071b8ef19b967c1a595999d2")

