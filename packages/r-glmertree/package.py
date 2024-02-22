# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmertree(RPackage):
	"""Generalized Linear Mixed Model Trees

	Recursive partitioning based on (generalized) linear mixed models
    (GLMMs) combining lmer()/glmer() from 'lme4' and lmtree()/glmtree() from 
    'partykit'. The fitting algorithm is described in more detail in Fokkema,
    Smits, Zeileis, Hothorn & Kelderman (2018; <DOI:10.3758/s13428-017-0971-x>).
	"""
	
	cran = "glmertree" 

	version("0.2-4", md5="0b79b7eddc095d543fc58ed5ea116ca1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-partykit@1.0.4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
