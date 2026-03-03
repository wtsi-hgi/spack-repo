# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfd(RPackage):
	"""Compute and Illustrate the Multiple Facets of Functional
Diversity

	Computing functional traits-based distances between pairs of 
    species for species gathered in assemblages allowing to build several
    functional spaces. The package allows to compute functional diversity
    indices assessing the distribution of species (and of their dominance) in a
    given functional space for each assemblage and the overlap between
    assemblages in a given functional space, see: Chao et al. (2018)
    <doi:10.1002/ecm.1343>, Maire et al. (2015) <doi:10.1111/geb.12299>,
    Mouillot et al. (2013) <doi:10.1016/j.tree.2012.10.004>, Mouillot et al.
    (2014) <doi:10.1073/pnas.1317625111>, Ricotta and Szeidl (2009)
    <doi:10.1016/j.tpb.2009.10.001>. Graphical outputs are included.
    Visit the 'mFD' website for more information, documentation and examples.
	"""
	
	homepage = "https://cmlmagneville.github.io/mFD/"
	cran = "mFD" 

	version("1.0.7", md5="1b32208ecb2bef045004a89b5cc89beb")
	version("1.0.6", md5="3671b2311dea3586dda152426e8ff26e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-betapart@1.5.4:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-gawdis", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
