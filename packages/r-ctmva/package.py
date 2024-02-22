# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtmva(RPackage):
	"""Continuous-Time Multivariate Analysis

	Implements a basis function or functional data analysis framework
             for several techniques of multivariate analysis in continuous-time 
             setting. Specifically, we introduced continuous-time analogues of
             several classical techniques of multivariate analysis, such as 
             principal component analysis, canonical correlation analysis, 
             Fisher linear discriminant analysis, K-means clustering, and so 
             on. Details are in Biplab Paul, Philip T. Reiss and Erjia Cui (2023) 
             "Continuous-time multivariate analysis" <doi:10.48550/arXiv.2307.09404>.
	"""
	
	cran = "ctmva" 

	version("1.4.0", md5="426a8f08935d1f4b40857170e00c0823")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
