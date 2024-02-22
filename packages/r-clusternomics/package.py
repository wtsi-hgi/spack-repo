# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusternomics(RPackage):
	"""Integrative Clustering for Heterogeneous Biomedical Datasets

	Integrative context-dependent clustering for heterogeneous
    biomedical datasets. Identifies local clustering structures in related
    datasets, and a global clusters that exist across the datasets.
	"""
	
	homepage = "https://github.com/evelinag/clusternomics"
	cran = "clusternomics" 

	version("0.1.1", md5="bb3de89be59e4ac298391c57dac0ada4")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
