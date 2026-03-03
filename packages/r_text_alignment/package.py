# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextAlignment(RPackage):
	"""Text Alignment with Smith-Waterman

	Find similarities between texts using the Smith-Waterman algorithm. The algorithm performs local sequence alignment and determines similar regions between two strings.
    The Smith-Waterman algorithm is explained in the paper: "Identification of common molecular subsequences" by T.F.Smith and M.S.Waterman (1981), available at <doi:10.1016/0022-2836(81)90087-5>. 
    This package implements the same logic for sequences of words and letters instead of molecular sequences.
	"""
	
	homepage = "https://github.com/DIGI-VUB/text.alignment"
	cran = "text.alignment" 

	version("0.1.4", md5="ca14db12b2d0b3721958950c9244e009")

	depends_on("r-rcpp", type=("build", "run"))
