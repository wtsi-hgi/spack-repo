# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlfd(RPackage):
	"""Portmanteau Local Feature Discrimination for Matrix-Variate Data

	
    The portmanteau local feature discriminant approach first identifies the local 
    discriminant features and their differential structures, then constructs the 
    discriminant rule by pooling the identified local features together. This method 
    is applicable to high-dimensional matrix-variate data. 
    See the paper by Xu, Luo and Chen (2021, <doi:10.1007/s13171-021-00255-2>).
	"""
	
	homepage = "https://github.com/paradoxical-rhapsody/PLFD"
	cran = "PLFD" 

	version("0.2.0", md5="8cfe971812d501faebe7ef1da7467256")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@1.0.2:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.800:", type=("build", "run"))
