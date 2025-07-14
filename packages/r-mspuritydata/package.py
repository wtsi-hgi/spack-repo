# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMspuritydata(RPackage):
	"""Fragmentation spectral libraries and data to test the msPurity package

	Fragmentation spectral libraries and data to test the msPurity package
	"""
	
	bioc = "msPurityData"

	version("1.36.0", commit="02a305aff24764b10048417051c5a663f3cad0b8")
	version("1.30.0", commit="0d2354278c3c4320465d354220cc0fadfd1f6c0f")


