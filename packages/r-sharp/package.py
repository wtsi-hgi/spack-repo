# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharp(RPackage):
	"""Stability-enHanced Approaches using Resampling Procedures

	In stability selection (N Meinshausen, P Bühlmann (2010) <doi:10.1111/j.1467-9868.2010.00740.x>) and consensus clustering (S Monti et al (2003) <doi:10.1023/A:1023949509487>), resampling techniques are used to enhance the reliability of the results. In this package, hyper-parameters are calibrated by maximising model stability, which is measured under the null hypothesis that all selection (or co-membership) probabilities are identical (B Bodinier et al (2023a) <doi:10.1093/jrsssc/qlad058> and B Bodinier et al (2023b) <doi:10.1093/bioinformatics/btad635>). Functions are readily implemented for the use of LASSO regression, sparse PCA, sparse (group) PLS or graphical LASSO in stability selection, and hierarchical clustering, partitioning around medoids, K means or Gaussian mixture models in consensus clustering. 
	"""
	
	homepage = "https://github.com/barbarabodinier/sharp"
	cran = "sharp" 

	version("1.4.6", md5="b44e0d21ab2c831371fc59a356aa48d4")

	depends_on("r-fake@1.4:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-glassofast@1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-withr@2.4:", type=("build", "run"))
