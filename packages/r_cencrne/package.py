# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCencrne(RPackage):
	"""Consistent Estimation of the Number of Communities via
Regularized Network Embedding

	The network analysis plays an important role in numerous application domains including biomedicine. 
             Estimation of the number of communities is a fundamental and critical issue in network analysis. Most existing studies assume that the number of communities is known a priori, or lack of rigorous theoretical guarantee on the estimation consistency. This method proposes a regularized network embedding model to simultaneously estimate the community structure and the number of communities in a unified formulation. 
	           The proposed model equips network embedding with a novel composite regularization term, which pushes the embedding vector towards its center and collapses similar community centers with each other. A rigorous theoretical analysis is conducted, establishing asymptotic consistency in terms of community detection and estimation of the number of communities. 
	           Reference: 
             Ren, M., Zhang S. and Wang J. (2022). "Consistent Estimation of the Number of Communities via Regularized Network Embedding". Biometrics, <doi:10.1111/biom.13815>.
	"""
	
	cran = "cencrne" 

	version("1.0.0", md5="dcfb7f7bbf62460d408d23c31a7bac26")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
