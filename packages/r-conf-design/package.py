# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfDesign(RPackage):
	"""Construction of factorial designs

	This small library contains a series of simple tools for
        constructing and manipulating confounded and fractional
        factorial designs.
	"""
	
	cran = "conf.design" 

	version("2.0.0", md5="b2c9aa7afe463356b9af6bb10fd1b2e6")

