# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWesanderson(RPackage):
	"""A Wes Anderson Palette Generator

	Palettes generated mostly from 'Wes Anderson' movies.
	"""
	
	homepage = "https://github.com/karthik/wesanderson"
	cran = "wesanderson" 

	version("0.3.7", md5="8becbb8ab06d2c694c06d0a1b10da95b")

	depends_on("r@3:", type=("build", "run"))
