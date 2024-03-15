# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmacof(RPackage):
	"""Multidimensional Scaling

	Implements the following approaches for multidimensional scaling (MDS) based on stress minimization using majorization (smacof): ratio/interval/ordinal/spline MDS on symmetric dissimilarity matrices, MDS with external constraints on the configuration, individual differences scaling (idioscal, indscal), MDS with spherical restrictions, and ratio/interval/ordinal/spline unfolding (circular restrictions, row-conditional). Various tools and extensions like jackknife MDS, bootstrap MDS, permutation tests, MDS biplots, gravity models, unidimensional scaling, drift vectors (asymmetric MDS), classical scaling, and Procrustes are implemented as well.  
	"""
	
	cran = "smacof" 

	version("2.1-6", md5="2fa58efcef18c1e5b7442823f1ec01f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-candisc", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
