# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTapkee(RPackage):
	"""Wrapper for 'tapkee' Dimension Reduction Library

	Wrapper for using 'tapkee' command line utility,
 it allows to run it from inside R and catch the results for further analysis and plotting.
 'Tapkee' is a program for fast dimension reduction, see 'package?tapkee' and <http://tapkee.lisitsyn.me/>
 for installation and other details.
	"""
	
	cran = "tapkee" 

	version("1.2", md5="6942045145670833ee2c062d6df8fb56")

