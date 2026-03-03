# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInquilab(RPackage):
	"""Dissipation Kinetics Analysis, Half Life Period, Rate Constant,
Plots

	For environmental chemists, ecologists, researchers and agricultural scientists to understand the dissipation kinetics, calculate the half-life periods and rate constants of compounds, pesticides, contaminants in different matrices.
	"""
	
	cran = "Inquilab" 

	version("0.1.0", md5="11aad6d1e88d535c9d66c5f3ec7de910")

