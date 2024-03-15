# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGasper(RPackage):
	"""Graph Signal Processing

	Provides the standard operations for signal processing on graphs: 
    graph Fourier transform, spectral graph wavelet transform, 
    visualization tools. It also implements a data driven method
    for graph signal denoising/regression, for details see 
    De Loynes, Navarro, Olivier (2019) <arxiv:1906.01882>. 
    The package also provides an interface to the SuiteSparse Matrix Collection, 
    <https://sparse.tamu.edu/>, a large and widely used set of sparse matrix 
    benchmarks collected from a wide range of applications.
	"""
	
	homepage = "https://github.com/fabnavarro/gasper"
	cran = "gasper" 

	version("1.1.6", md5="1dabbc698d5d099ad1f7c43f91fe575d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
