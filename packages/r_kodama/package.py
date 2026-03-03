# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKodama(RPackage):
	"""Knowledge Discovery by Accuracy Maximization

	An unsupervised and semi-supervised learning algorithm that performs feature extraction 
  from noisy and high-dimensional data. It facilitates identification of patterns representing underlying 
  groups on all samples in a data set. Based on Cacciatore S, Tenori L, Luchinat C, Bennett PR, MacIntyre DA. 
  (2017) Bioinformatics <doi:10.1093/bioinformatics/btw705> and Cacciatore S, Luchinat C, Tenori L. (2014) 
  Proc Natl Acad Sci USA <doi:10.1073/pnas.1220873111>.
	"""
	
	cran = "KODAMA" 

	version("2.4", md5="13db2df949879b8c4bad86d23a752a66")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
