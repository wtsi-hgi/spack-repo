# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdiffcom(RPackage):
	"""Differential Analysis of Intercellular Communication from
scRNA-Seq Data

	Analysis tools to investigate changes in intercellular
    communication from scRNA-seq data. Using a Seurat object as input,
    the package infers which cell-cell interactions are present in the dataset
    and how these interactions change between two conditions of interest
    (e.g. young vs old). It relies on an internal database of ligand-receptor
    interactions (available for human, mouse and rat) that have been gathered
    from several published studies. Detection and differential analyses
    rely on permutation tests. The package also contains several tools
    to perform over-representation analysis and visualize the results. See
    Lagger, C. et al. (2023) <doi:10.1038/s43587-023-00514-x> for a full 
    description of the methodology.
	"""
	
	homepage = "https://cyrillagger.github.io/scDiffCom/"
	cran = "scDiffCom" 

	version("1.0.0", md5="1338b39bb33a907624363b17e43ff787")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-seurat@4:", type=("build", "run"))
