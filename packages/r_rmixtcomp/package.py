# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmixtcomp(RPackage):
	"""Mixture Models with Heterogeneous and (Partially) Missing Data

	Mixture Composer (Biernacki (2015) <https://inria.hal.science/hal-01253393v1>) is a project to perform clustering using mixture models with
    heterogeneous data and partially missing data. Mixture models are fitted using a SEM algorithm.
    It includes 8 models for real, categorical, counting, functional and ranking data.
	"""
	
	homepage = "https://github.com/modal-inria/MixtComp"
	cran = "RMixtComp" 

	version("4.1.4", md5="cfc44ce274c747b2037729e0a361fedb")

	depends_on("r-rmixtcomputilities@4.1.4:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmixtcompio@4.0.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
