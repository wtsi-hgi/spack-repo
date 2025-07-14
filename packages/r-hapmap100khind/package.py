# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap100khind(RPackage):
	"""Sample data - Hapmap 100K HIND Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap100khind"

	version("1.50.0", commit="cf1ac792be6e4c2789861039756ccf427d8aac92")
	version("1.44.0", commit="b17b43fd18098f41c1be8e9b1d6b660f4a6dde3b")


