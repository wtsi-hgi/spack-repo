# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImportar(RPackage):
	"""Enables Importing/Loading of Packages or Functions While
Creating an Alias for Them

	Enables 'Python'-like importing/loading of packages or functions
    with aliasing to prevent namespace conflicts.
	"""
	
	homepage = "https://github.com/andreaphsz/importar"
	cran = "importar" 

	version("0.1.1", md5="6ba75aaeca82ce4a3ae2d20ff2c223e5")

