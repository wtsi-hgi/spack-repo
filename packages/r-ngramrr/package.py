# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgramrr(RPackage):
	"""A Simple General Purpose N-Gram Tokenizer

	A simple n-gram (contiguous sequences of n items from a
    given sequence of text) tokenizer to be used with the 'tm' package with no
    'rJava'/'RWeka' dependency.
	"""
	
	homepage = "https://github.com/chainsawriot/ngramrr"
	cran = "ngramrr" 

	version("0.2.0", md5="db447c93343d4a138f74ef91eeb794e9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-tau", type=("build", "run"))
