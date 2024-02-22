# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsa(RPackage):
	"""Latent Semantic Analysis

	The basic idea of latent semantic analysis (LSA) is, 
  that text do have a higher order (=latent semantic) structure which, 
  however, is obscured by word usage (e.g. through the use of synonyms 
  or polysemy). By using conceptual indices that are derived statistically 
  via a truncated singular value decomposition (a two-mode factor analysis) 
  over a given document-term matrix, this variability problem can be overcome. 
	"""
	
	cran = "lsa" 

	version("0.73.3", md5="205b9add99f5a37f1cf93567ec73c5e0")

	depends_on("r-snowballc", type=("build", "run"))
