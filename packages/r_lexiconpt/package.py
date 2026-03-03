# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexiconpt(RPackage):
	"""Lexicons for Portuguese Text Analysis

	Provides easy access for sentiment lexicons for those who want to do text analysis in Portuguese texts.
    As of now, two Portuguese lexicons are available: 'SentiLex-PT02' and 'OpLexicon' (v2.1 and v3.0).
	"""
	
	cran = "lexiconPT" 

	version("0.1.0", md5="2b28a31e9f3e43fa7cbbd58eb66f4281")

	depends_on("r@2.10:", type=("build", "run"))
