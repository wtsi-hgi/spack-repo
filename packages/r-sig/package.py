# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSig(RPackage):
	"""Print Function Signatures

	Print function signatures and find overly complicated code.
	"""
	
	homepage = "https://bitbucket.org/richierocks/sig"
	cran = "sig" 

	version("0.0-6", md5="b2f704cbde5d18544ddf5d27fa45e9ff")

	depends_on("r@2.15:", type=("build", "run"))
