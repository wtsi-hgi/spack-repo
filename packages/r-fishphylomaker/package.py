# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishphylomaker(RPackage):
	"""Phylogenies for a List of Finned-Ray Fishes

	Provides an alternative to facilitate the construction of a phylogeny for fish species from a list of species
   or a community matrix using as a backbone the phylogenetic tree proposed by Rabosky et al. (2018) <doi:10.1038/s41586-018-0273-1>.
	"""
	
	cran = "FishPhyloMaker" 

	version("0.2.0", md5="3d5ecb64a36231ccfa6c04c7a0e4df75")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-fishtree", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rfishbase", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
