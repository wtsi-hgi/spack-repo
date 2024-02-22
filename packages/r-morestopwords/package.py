# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorestopwords(RPackage):
	"""All Stop Words in One Place

	A standalone package combining several stop-word lists for 65 languages with a median of 329 stop words for language and over 1,000 entries for English, Breton, Latin, Slovenian, and Ancient Greek! The user automatically gets access to all the unique stop words contained in: the 'StopwordISO' repository; the 'Natural Language Toolkit' for 'python'; the 'Snowball' stop-word list; the R package 'quanteda'; the 'marimo' repository; the 'Perseus' project; and A. Berra's list of stop words for Ancient Greek and Latin.
	"""
	
	homepage = "https://fatelarico.github.io/morestopwords.html"
	cran = "morestopwords" 

	version("0.2.0", md5="abee5a9ca68e04707522c37a2fb3bc4a")

	depends_on("r@2.10:", type=("build", "run"))
