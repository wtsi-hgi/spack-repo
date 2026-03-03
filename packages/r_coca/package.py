# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoca(RPackage):
	"""Cluster-of-Clusters Analysis

	Contains the R functions needed to perform Cluster-Of-Clusters Analysis (COCA)  and Consensus Clustering (CC). For further details please see Cabassi and Kirk (2020) <doi:10.1093/bioinformatics/btaa593>.
	"""
	
	homepage = "http://github.com/acabassi/coca"
	cran = "coca" 

	version("1.1.0", md5="b84e2b5c3c97bd1d21422de6b30bf3e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sparcl", type=("build", "run"))
