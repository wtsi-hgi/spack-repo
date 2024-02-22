# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordpieceData(RPackage):
	"""Data for Wordpiece-Style Tokenization

	Provides data to be used by the wordpiece algorithm in order to 
    tokenize text into somewhat meaningful chunks. Included vocabularies were 
    retrieved from 
    <https://huggingface.co/bert-base-cased/resolve/main/vocab.txt> and 
    <https://huggingface.co/bert-base-uncased/resolve/main/vocab.txt> and parsed
    into an R-friendly format.
	"""
	
	homepage = "https://github.com/macmillancontentscience/wordpiece.data"
	cran = "wordpiece.data" 

	version("2.0.0", md5="08930bfbb4d76d818d8576295b7e102b")

	depends_on("r@3.5:", type=("build", "run"))
