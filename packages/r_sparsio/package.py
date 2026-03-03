# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsio(RPackage):
	"""I/O Operations with Sparse Matrices

	Fast 'SVMlight' reader and writer. 
    'SVMlight' is most commonly used format for storing 
    sparse matrices (possibly with some target variable) on disk.
    For additional information about 'SVMlight' format see <http://svmlight.joachims.org/>.
	"""
	
	homepage = "https://github.com/dselivanov/sparsio"
	cran = "sparsio" 

	version("1.0.1", md5="77d8b6de69ff6a525fdcfe3a8b4730fb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.1:", type=("build", "run"))
