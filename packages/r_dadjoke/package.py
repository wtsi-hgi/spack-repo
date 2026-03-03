# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDadjoke(RPackage):
	"""Displays a Dad Joke

	Displays a terrible joke, the kind only dads crack.
	"""
	
	cran = "dadjoke" 

	version("1.0", md5="d25ce4b17d0eeb44ecc0a3ac5c16a7f9")

	depends_on("r@3:", type=("build", "run"))
