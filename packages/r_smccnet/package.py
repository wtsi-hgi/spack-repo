# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmccnet(RPackage):
	"""Sparse Multiple Canonical Correlation Network Analysis Tool

	
   A canonical correlation based framework (SmCCNet) designed for the construction of phenotype-specific multi-omics networks. This framework adeptly integrates single or multiple omics data types along with a quantitative or binary phenotype of interest. It offers a streamlined setup process that can be tailored manually or configured automatically, ensuring a flexible and user-friendly experience.
	"""
	
	homepage = "https://github.com/KechrisLab/SmCCNet"
	cran = "SmCCNet" 

	version("2.0.2", md5="c033e2c178d35ac9f6dd4bf4a84c74ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-spls", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
