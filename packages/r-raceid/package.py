# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaceid(RPackage):
	"""Identification of Cell Types, Inference of Lineage Trees, and
Prediction of Noise Dynamics from Single-Cell RNA-Seq Data

	Application of 'RaceID' allows inference of cell types and prediction of lineage trees by the 'StemID2' algorithm (Herman, J.S., Sagar, Grun D. (2018) <DOI:10.1038/nmeth.4662>). 'VarID2' is part of this package and allows quantification of biological gene expression noise at single-cell resolution (Rosales-Alvarez, R.E., Rettkowski, J., Herman, J.S., Dumbovic, G., Cabezas-Wallscheid, N., Grun, D. (2023) <DOI:10.1186/s13059-023-02974-1>).
	"""
	
	cran = "RaceID" 

	version("0.3.4", md5="61333d00e6b58c1815cd3a24b763a813")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fateid", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-leiden", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-runner", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
