# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustmd(RPackage):
	"""Model Based Clustering for Mixed Data

	Model-based clustering of mixed data (i.e. data which consist of
    continuous, binary, ordinal or nominal variables) using a parsimonious
    mixture of latent Gaussian variable models.
	"""
	
	cran = "clustMD" 

	version("1.2.1", md5="35886c3d4dcef7c33ec3bcf4c665e36c")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
