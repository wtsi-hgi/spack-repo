# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextometry(RPackage):
	"""Textual Data Analysis Package Used by the TXM Software

	Statistical exploration of textual corpora using several methods
    from French 'Textometrie' (new name of 'Lexicometrie') and French 'Data Analysis' schools.
    It includes methods for exploring irregularity of distribution of lexicon features across
    text sets or parts of texts (Specificity analysis); multi-dimensional exploration (Factorial analysis), etc. 
    Those methods are used in the TXM software.
	"""
	
	cran = "textometry" 

	version("0.1.6", md5="f93eb68c5edf1c0a3dc5f376880b5381")

	depends_on("r@1.5:", type=("build", "run"))
