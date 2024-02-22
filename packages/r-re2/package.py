# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRe2(RPackage):
	"""R Interface to Google RE2 (C++) Regular Expression Library

	Pattern matching, extraction, replacement and other string
  processing operations using Google's RE2 <https://github.com/google/re2>
  regular-expression engine. Consistent interface (similar to 'stringr').
  RE2 uses finite-automata based techniques, and offers a
  fast and safe alternative to backtracking regular-expression engines
  like those used in 'stringr', 'stringi' and other PCRE implementations.
	"""
	
	homepage = "https://github.com/girishji/re2"
	cran = "re2" 

	version("0.1.3", md5="f9988569a81368be887277bbe1906ee8", url="https://cran.r-project.org/src/contrib/re2_0.1.3.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
