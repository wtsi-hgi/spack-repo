# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmre(RPackage):
	"""Parallelized Minimum Redundancy, Maximum Relevance (mRMR)

	Computes mutual information matrices from continuous, categorical 
  and survival variables, as well as feature selection with minimum redundancy, 
  maximum relevance (mRMR) and a new ensemble mRMR technique. Published in
  De Jay et al. (2013) <doi:10.1093/bioinformatics/btt383>.
	"""
	
	homepage = "https://www.pmgenomics.ca/bhklab/"
	cran = "mRMRe" 

	version("2.1.2.1", md5="d9c34a068da782a682d9bed2d11f62d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
