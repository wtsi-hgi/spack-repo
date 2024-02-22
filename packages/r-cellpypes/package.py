# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellpypes(RPackage):
	"""Cell Type Pipes for Single-Cell RNA Sequencing Data

	Annotate single-cell RNA sequencing data manually based on
    marker gene thresholds.
    Find cell type rules (gene+threshold) through exploration,
    use the popular piping operator '%>%' to reconstruct complex
    cell type hierarchies.
    'cellpypes' models technical noise to find positive and negative cells for
    a given expression threshold and returns cell type labels or pseudobulks.
    Cite this package as Frauhammer (2022) <doi:10.5281/zenodo.6555728> and
    visit <https://github.com/FelixTheStudent/cellpypes> for tutorials and newest
    features.
	"""
	
	homepage = "https://github.com/FelixTheStudent/cellpypes"
	cran = "cellpypes" 

	version("0.3.0", md5="cb2c71ad2f014dac3493e081ac0d059d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-scutils", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
