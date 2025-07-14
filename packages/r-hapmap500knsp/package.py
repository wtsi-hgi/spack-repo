# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap500knsp(RPackage):
	"""Sample data - Hapmap 500K NSP Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap500knsp"

	version("1.50.0", commit="4db326e73355eb1b76f04088d838bc06d808e89c")
	version("1.44.0", commit="1ee33b5ac12f3e2d8e53cb1fbb5f607c05f6635d")


