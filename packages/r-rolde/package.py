# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolde(RPackage):
	"""RolDE: Robust longitudinal Differential Expression

	RolDE detects longitudinal differential expression between two conditions in noisy high-troughput data. Suitable even for data with a moderate amount of missing values.RolDE is a composite method, consisting of three independent modules with different approaches to detecting longitudinal differential expression. The combination of these diverse modules allows RolDE to robustly detect varying differences in longitudinal trends and expression levels in diverse data types and experimental settings.
	"""
	
	homepage = "https://github.com/elolab/RolDE"
	bioc = "RolDE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RolDE_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RolDE/RolDE_1.6.0.tar.gz"]

	version("1.6.0", md5="12c19e976fa6e9be2e9fa9a433690355")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rots", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rngtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
