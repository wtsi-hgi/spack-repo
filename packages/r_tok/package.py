# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTok(RPackage):
	"""Fast Text Tokenization

	
  Interfaces with the 'Hugging Face' tokenizers library to provide implementations
  of today's most used tokenizers such as the 'Byte-Pair Encoding' algorithm 
  <https://huggingface.co/docs/tokenizers/index>. It's extremely fast for both 
  training new vocabularies and tokenizing texts.
	"""
	
	homepage = "https://github.com/mlverse/tok"
	cran = "tok" 

	version("0.1.1", md5="b09ef590b34df13e1fdcc384998ef4fe")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
	depends_on("llvm", type=("build", "link", "run"))
