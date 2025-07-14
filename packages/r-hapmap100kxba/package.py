# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap100kxba(RPackage):
	"""Sample data - Hapmap 100K XBA Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap100kxba"

	version("1.50.0", commit="5e54b85ed5112a8e8205e673413ae44d281c4868")
	version("1.44.0", commit="79f7a14f331bdcdabae0a0a1984ad122570e4d18")


