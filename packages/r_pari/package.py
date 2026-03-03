# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPari(RPackage):
	"""Permutation-Based All-Resolutions Inference Method

	It computes the All-Resolution Inference method in the permutation framework, i.e., simultaneous lower confidence bounds for the number of true discoveries. <arXiv:2012.00368>. 
	"""
	
	homepage = "https://github.com/angeella/pARI"
	cran = "pARI" 

	version("1.1.1", md5="8b2381e944904a43836893a3ed4e8cfd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-aribrain", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
