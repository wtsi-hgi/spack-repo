# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmapsnp5(RPackage):
	"""Sample data - Hapmap SNP 5.0 Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmapsnp5"

	version("1.50.0", commit="cdb91e3d7740f78cc557f6034b9279c0a6bc09cb")
	version("1.44.0", commit="42c2690275ea0cc939893eaa19a7d131e1adddd0")


