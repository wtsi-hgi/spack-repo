# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCetcolor(RPackage):
	"""CET Perceptually Uniform Colour Maps

	Collection of perceptually uniform colour maps made by Peter Kovesi
    (2015) "Good Colour Maps: How to Design Them" <arXiv:1509.03700> 
    at the Centre for Exploration Targeting (CET).
	"""
	
	homepage = "https://github.com/coatless/cetcolor"
	cran = "cetcolor" 

	version("0.2.0", md5="767e99170570e1700e096f85d96c0dc2")

	depends_on("r@3.3:", type=("build", "run"))
