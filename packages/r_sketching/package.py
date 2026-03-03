# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSketching(RPackage):
	"""Sketching of Data via Random Subspace Embeddings

	Construct sketches of data via random subspace embeddings. 
  For more details, see the following papers.
  Lee, S. and Ng, S. (2022). "Least Squares Estimation Using Sketched Data with Heteroskedastic Errors," Proceedings of the 39th International Conference on Machine Learning (ICML22), 162:12498-12520.
  Lee, S. and Ng, S. (2020). "An Econometric Perspective on Algorithmic Subsampling," Annual Review of Economics, 12(1): 45–80.
	"""
	
	homepage = "https://github.com/sokbae/sketching/"
	cran = "sketching" 

	version("0.1.2", md5="c5c34f0e0d1712a0a4056d2113a89675")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-phangorn@2.8.1:", type=("build", "run"))
