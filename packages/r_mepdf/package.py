# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMepdf(RPackage):
	"""Creation of Empirical Density Functions Based on Multivariate
Data

	Based on the input data an n-dimensional cube with sub cells of user specified side length is created.
    The number of sample points which fall in each sub cube is counted, and with the cell volume and overall sample
    size an empirical probability can be computed. A number of cubes of higher resolution can be superimposed. The
    basic method stems from J.L. Bentley in "Multidimensional Divide and Conquer".
    J. L. Bentley (1980) <doi:10.1145/358841.358850>.
    Furthermore a simple kernel density estimation method is made available, as well as an expansion of Bentleys
    method, which offers a kernel approach for the grid method.
	"""
	
	cran = "MEPDF" 

	version("3.0", md5="f2b7d48c7d9100462d83d183f80722e5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
