# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListarrays(RPackage):
	"""A Toolbox for Working with R Arrays in a Functional Programming
Style

	A toolbox for R arrays. Flexibly split, bind, reshape, modify, 
    subset and name arrays.
	"""
	
	homepage = "https://github.com/t-kalinowski/listarrays"
	cran = "listarrays" 

	version("0.3.1", md5="f3a7d318b2d06498788249252afa149d")

