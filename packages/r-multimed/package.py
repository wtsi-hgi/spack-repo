# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimed(RPackage):
	"""Testing multiple biological mediators simultaneously

	Implements methods for testing multiple mediators
	"""
	
	bioc = "MultiMed"

	version("2.30.0", commit="5b47208e1b600c9ede85fa494a753680f05e4e48")
	version("2.24.0", commit="f8c3d5cf3326f816672f76ea78d8153d427c7cee")

	depends_on("r@3.1:", type=("build", "run"))
