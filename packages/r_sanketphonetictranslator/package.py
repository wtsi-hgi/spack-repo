# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanketphonetictranslator(RPackage):
	"""Phonetic Transliteration Between Hindi and English

	Facilitate phonetic transliteration between different languages. With support for both Hindi and English, this package provides a way to convert text between Hindi and English dataset. Whether you're working with multilingual data or need to convert dataset for analysis or presentation purposes, it offers a simple and efficient solution and harness the power of phonetic transliteration in your projects with this versatile package.
	"""
	
	cran = "sanketphonetictranslator" 

	version("0.1.0", md5="0b636ea163e3dffd7ff32064dd46501f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
