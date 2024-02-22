# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlputils(RPackage):
	"""Natural Language Processing Utilities

	Utilities for Natural Language Processing.
	"""
	
	cran = "NLPutils" 

	version("0.0-5.1", md5="022355f6f0cffeef966a669bc8aff08e")

	depends_on("r-nlp@0.1.11.3:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-qdap", type=("build", "run"))
