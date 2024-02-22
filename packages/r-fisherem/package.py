# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFisherem(RPackage):
	"""The FisherEM Algorithm to Simultaneously Cluster and Visualize
High-Dimensional Data

	The FisherEM algorithm, proposed by Bouveyron & Brunet (2012) <doi:10.1007/s11222-011-9249-9>,
        is an efficient method for the clustering of high-dimensional data. FisherEM models and 
        clusters the data in a discriminative and low-dimensional latent subspace. It also provides
        a low-dimensional representation of the clustered data. A sparse version of Fisher-EM
        algorithm is also provided.
	"""
	
	cran = "FisherEM" 

	version("1.6", md5="0b005b1f517703d76fbf42b354515376")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
