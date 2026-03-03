# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelwordcloud(RPackage):
	"""Model Word Clouds

	Makes a word cloud of text, sized by the frequency of the word, and colored either by user-specified colors or colored by the strength of the coefficient of that text derived from a regression model.
	"""
	
	cran = "modelwordcloud" 

	version("0.1", md5="838f5ce9f8232b68237428b1a1c621ea")

