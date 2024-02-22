# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchoenberg(RPackage):
	"""Tools for 12-Tone Musical Composition

	Functions for creating and manipulating 12-tone (i.e., dodecaphonic) musical matrices using Arnold Schoenberg's (1923) serialism technique. This package can generate random 12-tone matrices and can generate matrices using a pre-determined sequence of notes. 
	"""
	
	cran = "schoenberg" 

	version("2.0.3", md5="5c7fd4e14e1b1b0a652355dd8ae36380")

	depends_on("r-crayon", type=("build", "run"))
