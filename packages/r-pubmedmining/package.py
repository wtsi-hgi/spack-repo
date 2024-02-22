# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubmedmining(RPackage):
	"""Text-Mining of the 'PubMed' Repository

	Easy function for text-mining the 'PubMed' repository based on defined sets of terms.
    The relationship between fix-terms (related to your research topic) and pub-terms (terms which pivot around your research focus)
    is calculated using the pointwise mutual information algorithm ('PMI'). Church, Kenneth Ward and Hanks, Patrick (1990) <https://www.aclweb.org/anthology/J90-1003/>
    A text file is generated with the 'PMI'-scores for each fix-term. Then for each collocation pairs (a fix-term + a pub-term),
    a text file is generated with related article titles and publishing years. Additional Author section will follow in the next version updates.
	"""
	
	cran = "PubMedMining" 

	version("1.0.0", md5="f1f3fe366d133ce429b50a030c63e901")

	depends_on("r-easypubmed", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
