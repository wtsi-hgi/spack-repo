# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsaur(RPackage):
	"""A Handbook of Statistical Analyses Using R (1st Edition)

	Functions, data sets, analyses and examples from the book 
  ''A Handbook of Statistical Analyses Using R'' (Brian S. Everitt and Torsten
  Hothorn, Chapman & Hall/CRC, 2006). The first chapter
  of the book, which is entitled ''An Introduction to R'', 
  is completely included in this package, for all other chapters,
  a vignette containing all data analyses is available.
	"""
	
	cran = "HSAUR" 

	version("1.3-10", md5="f015a37af8f49a2f09e49bec01aa6b1e")

	depends_on("r@2.2:", type=("build", "run"))
