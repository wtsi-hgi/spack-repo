# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTokenizersBpe(RPackage):
	"""Byte Pair Encoding Text Tokenization

	Unsupervised text tokenizer focused on computational efficiency. Wraps the 'YouTokenToMe' library <https://github.com/VKCOM/YouTokenToMe> which is an implementation of fast Byte Pair Encoding (BPE) <https://aclanthology.org/P16-1162/>.
	"""
	
	homepage = "https://github.com/bnosac/tokenizers.bpe"
	cran = "tokenizers.bpe" 

	version("0.1.3", md5="832e5952a66f32bae718cd1d88b2fff4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
