# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmecabko(RPackage):
	"""An 'Rcpp' Interface for Eunjeon Project

	An 'Rcpp' interface for Eunjeon project <http://eunjeon.blogspot.com/>.
    The 'mecab-ko' and 'mecab-ko-dic' is based on a C++ library,
    and part-of-speech tagging with them is useful when the spacing of source Korean text is not correct.
    This package provides part-of-speech tagging and tokenization function for Korean text.
	"""
	
	cran = "RmecabKo" 

	version("0.1.6.2", md5="6ab04875563dc7c99afe7a64d0a7105c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
