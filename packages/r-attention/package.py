# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttention(RPackage):
	"""Self-Attention Algorithm

	Self-Attention algorithm helper functions and demonstration vignettes of increasing depth on how to construct the Self-Attention algorithm, this is based on Vaswani et al. (2017) <doi:10.48550/arXiv.1706.03762>, Dan Jurafsky and James H. Martin (2022, ISBN:978-0131873216) <https://web.stanford.edu/~jurafsky/slp3/> "Speech and Language Processing (3rd ed.)" and Alex Graves (2020) <https://www.youtube.com/watch?v=AIiwuClvH6k> "Attention and Memory in Deep Learning".
	"""
	
	cran = "attention" 

	version("0.4.0", md5="6920730d0265d2188002c7a25158d8e4")

