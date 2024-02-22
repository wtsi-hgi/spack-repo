# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaststepgraph(RPackage):
	"""A Fast Algorithm for Sparse Precision Matrix Estimation

	It implements an improved and computationally faster version 
            of the original Stepwise Gaussian Graphical Algorithm for estimating 
            the Omega precision matrix from high-dimensional data. 
            Zamar, R., Ruiz, M., Lafit, G. and Nogales, J. (2021) 
            <doi:10.52933/jdssv.v1i2.11>.
	"""
	
	homepage = "https://github.com/juancolonna/FastStepGraph"
	cran = "FastStepGraph" 

	version("0.1.1", md5="ba50a937e2dad9455b8312c22910f22b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-doparallel@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
