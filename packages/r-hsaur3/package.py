# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsaur3(RPackage):
	"""A Handbook of Statistical Analyses Using R (3rd Edition)

	Functions, data sets, analyses and examples from the 
  third edition of the book 
  ''A Handbook of Statistical Analyses Using R'' (Torsten Hothorn and Brian S.
  Everitt, Chapman & Hall/CRC, 2014). The first chapter
  of the book, which is entitled ''An Introduction to R'', 
  is completely included in this package, for all other chapters,
  a vignette containing all data analyses is available. In addition,
  Sweave source code for slides of selected chapters is included in 
  this package (see HSAUR3/inst/slides). The publishers web page is 
  '<http://www.crcpress.com/product/isbn/9781482204582>'.
	"""
	
	cran = "HSAUR3" 

	version("1.0-14", md5="f2cd2053cefc5025deb4bdc0307249e1", url="https://cran.r-project.org/src/contrib/HSAUR3_1.0-14.tar.gz")

	depends_on("r@3:", type=("build", "run"))
