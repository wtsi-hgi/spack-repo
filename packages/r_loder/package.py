# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoder(RPackage):
	"""Dependency-Free Access to PNG Image Files

	Read and write access to PNG image files using the LodePNG
    library. The package has no external dependencies.
	"""
	
	homepage = "https://github.com/jonclayden/loder"
	cran = "loder" 

	version("0.2.1", md5="07ee60b41a730f551f95da3865d23760")

