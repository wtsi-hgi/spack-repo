# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirsm(RPackage):
	"""Inferring miRNA sponge modules in heterogeneous data

	The package aims to identify miRNA sponge modules in heterogeneous data. It provides several functions to study miRNA sponge modules, including popular methods for inferring gene modules (candidate miRNA sponge modules), and a function to identify miRNA sponge modules, as well as several functions to conduct modular analysis of miRNA sponge modules.
	"""
	
	homepage = "https://github.com/zhangjunpeng411/miRSM"
	bioc = "miRSM" 

    version("2.4.0", tag="RELEASE_3_21")
	version("1.20.0", commit="cfc3faaf7714fbd3f176bd415a5c3110b2da8e2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-flashclust", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-gfa", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-linkcomm", type=("build", "run"))
	depends_on("r-mcl", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-ibbig", type=("build", "run"))
	depends_on("r-fabia", type=("build", "run"))
	depends_on("r-bicare", type=("build", "run"))
	depends_on("r-isa2", type=("build", "run"))
	depends_on("r-s4vd", type=("build", "run"))
	depends_on("r-bibitr", type=("build", "run"))
	depends_on("r-rqubic", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-subspace", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-sombrero", type=("build", "run"))
	depends_on("r-ppclust", type=("build", "run"))
	depends_on("r-mirsponger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-matrixcorrelation", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
