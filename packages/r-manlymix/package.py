# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManlymix(RPackage):
	"""Manly Mixture Modeling and Model-Based Clustering

	The utility of this package includes finite mixture modeling and model-based clustering through Manly mixture models by Zhu and Melnykov (2016) <DOI:10.1016/j.csda.2016.01.015>. It also provides capabilities for forward and backward model selection procedures.  
	"""
	
	cran = "ManlyMix" 

	version("0.1.15", md5="8a4c9d6cb87c9b800c2a6bcc8b3c5f27")

	depends_on("r@3:", type=("build", "run"))
