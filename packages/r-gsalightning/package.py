# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsalightning(RPackage):
	"""Fast Permutation-based Gene Set Analysis

	GSALightning provides a fast implementation of permutation-based gene set analysis for two-sample problem. This package is particularly useful when testing simultaneously a large number of gene sets, or when a large number of permutations is necessary for more accurate p-values estimation.
	"""
	
	homepage = "https://github.com/billyhw/GSALightning"
	bioc = "GSALightning" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSALightning_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSALightning/GSALightning_1.30.0.tar.gz"]

	version("1.30.0", sha256="5fe9613d3acaebd43c1c678351d6d719007bd89d81201a2906401d4b2428c9c1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
