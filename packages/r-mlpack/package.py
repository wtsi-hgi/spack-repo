# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlpack(RPackage):
	"""'Rcpp' Integration for the 'mlpack' Library

	A fast, flexible machine learning library, written in C++, that
             aims to provide fast, extensible implementations of cutting-edge
             machine learning algorithms.  See also Curtin et al. (2023)
             <doi:10.21105/joss.05026>.
	"""
	
	homepage = "https://www.mlpack.org/doc/mlpack-git/r_documentation.html"
	cran = "mlpack" 

	version("4.3.0", md5="3d84c4dcb73d8a146916aa7c5cb79993")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.800:", type=("build", "run"))
	depends_on("r-rcppensmallen@0.2.10:", type=("build", "run"))
	depends_on("gcc@5:", type=("build", "link", "run"))
