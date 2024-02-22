# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScinsight(RPackage):
	"""Interpretation of Heterogeneous Single-Cell Gene Expression Data

	We develop a novel matrix factorization tool named 'scINSIGHT' to jointly analyze multiple single-cell gene expression samples from biologically heterogeneous sources, such as different disease phases, treatment groups, or developmental stages. Given multiple gene expression samples from different biological conditions, 'scINSIGHT' simultaneously identifies common and condition-specific gene modules and quantify their expression levels in each sample in a lower-dimensional space. With the factorized results, the inferred expression levels and memberships of common gene modules can be used to cluster cells and detect cell identities, and the condition-specific gene modules can help compare functional differences in transcriptomes from distinct conditions. Please also see Qian K, Fu SW, Li HW, Li WV (2022) <doi:10.1186/s13059-022-02649-3>.
	"""
	
	homepage = "https://github.com/Vivianstats/scINSIGHT"
	cran = "scINSIGHT" 

	version("0.1.4", md5="22031d874e891ed589e454364b5c0fa7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
