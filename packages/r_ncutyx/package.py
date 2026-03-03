# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcutyx(RPackage):
	"""Clustering of Omics Data of Multiple Types with a Multilayer
Network Representation

	Omics data come in different forms: gene expression, methylation, copy number, protein measurements and more.
    'NCutYX' allows clustering of variables, of samples, and both variables and samples (biclustering),
    while incorporating the dependencies across multiple types of Omics data.
    (SJ Teran Hidalgo et al (2017), <doi:10.1186/s12864-017-3990-1>). 
	"""
	
	homepage = "https://github.com/Seborinos/NCutYX"
	cran = "NCutYX" 

	version("0.1.0", md5="2b8aa4c4d4443925be49c1cfaf824233")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet@2.0.5:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.6:", type=("build", "run"))
	depends_on("r-fields@9:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
