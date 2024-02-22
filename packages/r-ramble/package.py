# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamble(RPackage):
	"""Parser Combinator for R

	Parser generator for R using combinatory parsers. It
    is inspired by combinatory parsers developed in Haskell.
	"""
	
	homepage = "https://github.com/chappers/Ramble"
	cran = "Ramble" 

	version("0.1.1", md5="3d54ea9d8e91ec1609f07edf5676120d")

