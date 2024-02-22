# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPez(RPackage):
	"""Phylogenetics for the Environmental Sciences

	Eco-phylogenetic and community phylogenetic analyses.
    Keeps community ecological and phylogenetic data matched up and
    comparable using 'comparative.comm' objects. Wrappers for common
    community phylogenetic indices ('pez.shape', 'pez.evenness',
    'pez.dispersion', and 'pez.dissimilarity' metrics). Implementation
    of Cavender-Bares (2004) correlation of phylogenetic and
    ecological matrices ('fingerprint.regression'). Phylogenetic
    Generalised Linear Mixed Models (PGLMMs; 'pglmm') following Ives &
    Helmus (2011) and Rafferty & Ives (2013). Simulation of null
    assemblages, traits, and phylogenies ('scape', 'sim.meta.comm').
	"""
	
	cran = "pez" 

	version("1.2-4", md5="089273a349e9af05a2e2e3d3cc919f4e")

	depends_on("r-ape@3.1.4:", type=("build", "run"))
	depends_on("r-caper@0.5.2:", type=("build", "run"))
	depends_on("r-picante@1.6.2:", type=("build", "run"))
	depends_on("r-quantreg@5.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-vegan@2.0.10:", type=("build", "run"))
	depends_on("r-ade4@1.6.2:", type=("build", "run"))
	depends_on("r-fd@1.0.12:", type=("build", "run"))
	depends_on("r-matrix@1.1.4:", type=("build", "run"))
	depends_on("r-animation@2.4.0:", type=("build", "run"))
	depends_on("r-phytools@0.6.60:", type=("build", "run"))
