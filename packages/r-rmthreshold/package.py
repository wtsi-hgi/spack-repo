# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmthreshold(RPackage):
	"""Signal-Noise Separation in Random Matrices by using Eigenvalue
Spectrum Analysis

	An algorithm which can be used to determine an objective threshold for signal-noise separation in large random matrices (correlation matrices, mutual information matrices, network adjacency matrices) is provided. The package makes use of the results of Random Matrix Theory (RMT). The algorithm increments a suppositional threshold monotonically, thereby recording the eigenvalue spacing distribution of the matrix. According to RMT, that distribution undergoes a characteristic change when the threshold properly separates signal from noise. By using the algorithm, the modular structure of a matrix - or of the corresponding network - can be unraveled.  
	"""
	
	cran = "RMThreshold" 

	version("1.1", md5="1482304b2d29b1cfa5492ddb7d8c6fd6")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
