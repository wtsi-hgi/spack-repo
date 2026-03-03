# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsaur2(RPackage):
	"""A Handbook of Statistical Analyses Using R (2nd Edition)

	Functions, data sets, analyses and examples from the 
  second edition of the book 
  ''A Handbook of Statistical Analyses Using R'' (Brian S. Everitt and Torsten
  Hothorn, Chapman & Hall/CRC, 2008). The first chapter
  of the book, which is entitled ''An Introduction to R'', 
  is completely included in this package, for all other chapters,
  a vignette containing all data analyses is available. In addition,
  the package contains Sweave code for producing slides for selected
  chapters (see HSAUR2/inst/slides).
	"""
	
	cran = "HSAUR2" 

	version("1.1-20", md5="a658232501354f2f287e777156260f9b", url="https://cran.r-project.org/src/contrib/HSAUR2_1.1-20.tar.gz")

	depends_on("r@2.2:", type=("build", "run"))
