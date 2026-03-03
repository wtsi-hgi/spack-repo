# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSslr(RPackage):
	"""Semi-Supervised Classification, Regression and Clustering
Methods

	Providing a collection of techniques for semi-supervised 
    classification, regression and clustering. In semi-supervised problem, both labeled and unlabeled
    data are used to train a classifier. The package includes a collection of 
    semi-supervised learning techniques: self-training, co-training, democratic, 
    decision tree, random forest, 'S3VM' ... etc, with a fairly intuitive interface 
    that is easy to use.
	"""
	
	homepage = "https://dicits.ugr.es/software/SSLR/"
	cran = "SSLR" 

	version("0.9.3.3", md5="280bc0d9088f30d9ac5a29a7d03b5313")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rssl", type=("build", "run"))
	depends_on("r-conclust", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
