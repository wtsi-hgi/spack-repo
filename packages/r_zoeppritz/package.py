# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoeppritz(RPackage):
	"""Seismic Reflection and Scattering Coefficients

	Calculate and plot scattering matrix coefficients for plane waves at interface.
	"""
	
	cran = "zoeppritz" 

	version("1.0-9", md5="8c23655416dc0e33a7dd8a0b6654c5a7")

