# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeebodata(RPackage):
	"""HEEBO set and HEEBO controls.

	R objects describing the HEEBO oligo set.
	"""
	
	homepage = "http://alizadehlab.stanford.edu/"
	bioc = "HEEBOdata"

	version("1.46.0", commit="66e21551cab1eed7e28c9a3441d8c14ad5fd4a11")
	version("1.40.0", commit="e636e71d8b2c306e97a21a0ded1f39da1f813040")


