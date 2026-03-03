# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgram(RPackage):
	"""Fast n-Gram 'Tokenization'

	An n-gram is a sequence of n "words" taken, in order, from a
    body of text.  This is a collection of utilities for creating,
    displaying, summarizing, and "babbling" n-grams.  The
    'tokenization' and "babbling" are handled by very efficient C
    code, which can even be built as its own standalone library.
    The babbler is a simple Markov chain.  The package also offers
    a vignette with complete example 'workflows' and information about
    the utilities offered in the package.
	"""
	
	homepage = "https://github.com/wrathematics/ngram"
	cran = "ngram" 

	version("3.2.3", md5="ab8f72dbe0b0828b0bedc7d48e8401f1")

	depends_on("r@3:", type=("build", "run"))
