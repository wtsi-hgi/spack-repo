# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFortunes(RPackage):
	"""R Fortunes

	A collection of fortunes from the R community.
	"""
	
	cran = "fortunes" 

	version("1.5-4", md5="6084d3ba4c97ec8ed015231caa369c75")

