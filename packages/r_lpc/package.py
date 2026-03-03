# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpc(RPackage):
	"""Lassoed Principal Components for Testing Significance of
Features

	Implements the LPC method of Witten&Tibshirani(Annals of Applied Statistics 2008) for identification of significant genes in a microarray experiment.
	"""
	
	cran = "lpc" 

	version("1.0.2.1", md5="bf404d97488586fca034027a33ad02cc")

