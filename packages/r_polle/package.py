# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolle(RPackage):
	"""Policy Learning

	Framework for evaluating user-specified finite stage policies and learning realistic policies via doubly robust loss functions. Policy learning methods include doubly robust restricted Q-learning, sequential policy tree learning and outcome weighted learning. See Nordland and Holst (2022) <arXiv:2212.02335> for documentation and references.
	"""
	
	cran = "polle" 

	version("1.3", md5="53d452286f917cabf4a892972d387390")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-data-table@1.14.5:", type=("build", "run"))
	depends_on("r-lava@1.7:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-policytree@1.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-targeted", type=("build", "run"))
	depends_on("r-dyntxregime", type=("build", "run"))
