# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSt(RPackage):
	"""Shrinkage t Statistic and Correlation-Adjusted t-Score

	Implements the "shrinkage t" statistic 
   introduced in Opgen-Rhein and Strimmer (2007) <DOI:10.2202/1544-6115.1252> and 
   a shrinkage estimate of the "correlation-adjusted t-score" (CAT score) described 
   in Zuber and Strimmer (2009) <DOI:10.1093/bioinformatics/btp460>.  
   It also offers a convenient interface  to a number of other regularized 
   t-statistics commonly employed in high-dimensional case-control studies.    
	"""
	
	homepage = "https://strimmerlab.github.io/software/st/"
	cran = "st" 

	version("1.2.7", md5="3e3be3e686ec212731d0d83a661aa1aa")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-sda@1.3.8:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.17:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
