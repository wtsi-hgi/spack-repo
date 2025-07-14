# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap500ksty(RPackage):
	"""Sample data - Hapmap 500K STY Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap500ksty"

	version("1.50.0", commit="d3b650527e3a0ef5a38bb8f879fb843fadc0cb44")
	version("1.44.0", commit="ee58e13a08ccab2af64c5ceb44237b041625dcf0")


