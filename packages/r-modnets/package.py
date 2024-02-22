# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModnets(RPackage):
	"""Modeling Moderated Networks

	Methods for modeling moderator variables in cross-sectional, temporal, and multi-level networks. Includes model selection techniques and a variety of plotting functions. Implements the methods described by Swanson (2020) <https://www.proquest.com/openview/d151ab6b93ad47e3f0d5e59d7b6fd3d3>.
	"""
	
	homepage = "https://github.com/tswanson222/modnets"
	cran = "modnets" 

	version("0.9.0", md5="76c51545c747b5634178520b9f616527")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glinternet", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-interactiontest", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
