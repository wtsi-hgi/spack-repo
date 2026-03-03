# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanek(RPackage):
	"""Batch Correction of Single Cell Transcriptome Data

	Non-linear/linear hybrid method for batch-effect correction
    that uses Mutual Nearest Neighbors (MNNs) to identify similar cells between 
    datasets. Reference: Loza M. et al. (NAR Genomics and Bioinformatics, 2020) <doi:10.1093/nargab/lqac022>.
	"""
	
	homepage = "https://martinloza.github.io/Canek/"
	cran = "Canek" 

	version("0.2.5", md5="294f934ddbd5e99e9be05c51bd8d50c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-bluster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
