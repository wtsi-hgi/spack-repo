# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquivnoninf(RPackage):
	"""Testing for Equivalence and Noninferiority

	Making available in R the complete set of programs accompanying S. Wellek's (2010) monograph
             ''Testing Statistical Hypotheses of Equivalence and Noninferiority. Second Edition''
             (Chapman&Hall/CRC). 
	"""
	
	cran = "EQUIVNONINF" 

	version("1.0.2", md5="fa80df5a8941cbff16ed238a66920ee1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
