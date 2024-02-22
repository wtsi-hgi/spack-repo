# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloregion(RPackage):
	"""Biogeographic Regionalization and Macroecology

	Computational infrastructure for biogeography, community ecology,
    and biodiversity conservation (Daru et al. 2020) <doi:10.1111/2041-210X.13478>.
    It is based on the methods described in Daru et al. (2020) <doi:10.1038/s41467-020-15921-6>.
    The original conceptual work is described in Daru et al. (2017) <doi:10.1016/j.tree.2017.08.013>
    on patterns and processes of biogeographical regionalization. Additionally, the package
    contains fast and efficient functions to compute more standard conservation measures
    such as phylogenetic diversity, phylogenetic endemism, evolutionary distinctiveness
    and global endangerment, as well as compositional turnover (e.g., beta diversity).
	"""
	
	homepage = "https://github.com/darunabas/phyloregion"
	cran = "phyloregion" 

	version("1.0.8", md5="f203491f8312f67315ca19f0fe1f0b28")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-betapart", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-clustmixtype", type=("build", "run"))
	depends_on("r-maptpx", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-predicts", type=("build", "run"))
	depends_on("r-smoothr", type=("build", "run"))
