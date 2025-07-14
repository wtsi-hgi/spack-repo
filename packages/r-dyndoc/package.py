# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyndoc(RPackage):
	"""Dynamic document tools

	A set of functions to create and interact with dynamic documents and vignettes.
	"""
	
	bioc = "DynDoc"

	version("1.86.0", commit="287ac9abf1e7ce2ce2197e723e54166b164ed33a")
	version("1.80.0", commit="74e583928ff09de9f8cf5401a3a0dc80315b6774")

