# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDets(RPackage):
	"""Tissue-Specific Enrichment Analysis

	Tissue-specific enrichment analysis to assess lists of candidate genes or RNA-Seq expression profiles. Pei G., Dai Y., Zhao Z. Jia P. (2019) deTS: Tissue-Specific Enrichment Analysis to decode tissue specificity. Bioinformatics, In submission.
	"""
	
	cran = "deTS" 

	version("1.0", md5="398476bdbfd82183989b8bc7579d2a88")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
