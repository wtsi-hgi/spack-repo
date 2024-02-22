# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovfefe(RPackage):
	"""Covfefy Any Word, Sentence or Speech

	Converts any word, sentence or speech into Trump's infamous
  "covfefe" format. Reference: <https://www.nytimes.com/2017/05/31/us/politics/covfefe-trump-twitter.html>.
  Inspiration thanks to: <https://codegolf.stackexchange.com/questions/123685/covfefify-a-string>.
	"""
	
	homepage = "https://github.com/mkirch/covfefe"
	cran = "covfefe" 

	version("0.1.0", md5="839b4c43935114fe354fd769fe0335ae")

	depends_on("r-tokenizers", type=("build", "run"))
