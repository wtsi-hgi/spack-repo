# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJlctree(RPackage):
	"""Joint Latent Class Trees for Joint Modeling of Time-to-Event and
Longitudinal Data

	Implements the tree-based approach to joint modeling of time-to-event and longitudinal data. This approach looks for a tree-based partitioning such that within each estimated latent class defined by a terminal node, the time-to-event and longitudinal responses display a lack of association. See Zhang and Simonoff (2018) <arXiv:1812.01774>.
	"""
	
	cran = "jlctree" 

	version("0.0.2", md5="8abae14f21ac79f455d2872f1182ab6f")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
