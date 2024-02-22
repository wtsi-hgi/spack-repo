# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloraster(RPackage):
	"""Evolutionary Diversity Metrics for Raster Data

	Phylogenetic Diversity (PD, Faith 1992), Evolutionary Distinctiveness (ED, Isaac et al. 2007), Phylogenetic Endemism (PE, Rosauer et al. 2009; Laffan et al. 2016), and Weighted Endemism (WE, Laffan et al. 2016) for presence-absence raster.
    Faith, D. P. (1992) <doi:10.1016/0006-3207(92)91201-3>
    Isaac, N. J. et al. (2007) <doi:10.1371/journal.pone.0000296>
    Laffan, S. W. et al. (2016)  <doi:10.1111/2041-210X.12513>
    Rosauer, D. et al. (2009) <doi:10.1111/j.1365-294X.2009.04311.x>.
	"""
	
	homepage = "https://gabferreira.github.io/phyloraster/"
	cran = "phyloraster" 

	version("2.0.1", md5="4c14ca56a3c42088e302eebd3b991759")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-sesraster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
