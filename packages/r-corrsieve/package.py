# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrsieve(RPackage):
	"""Software for Summarising and Evaluating STRUCTURE Output

	Statistical summary of STRUCTURE output. STRUCTURE is a K-means clustering method for inferring population structure and assigning individuals to populations using genetic data. Pritchard JK, Stephens M, Donnelly PJ (2000) <DOI:10.1093/genetics/155.2.945>. <https://web.stanford.edu/group/pritchardlab/structure.html>.
	"""
	
	homepage = "https://github.com/campanam/rCorrSieve"
	cran = "corrsieve" 

	version("1.6-9", md5="9e8c2a323795f996aff9bb8082b87e17")

