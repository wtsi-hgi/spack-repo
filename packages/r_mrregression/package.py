# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrregression(RPackage):
	"""Regression Analysis for Very Large Data Sets via Merge and
Reduce

	Frequentist and Bayesian linear regression for large data sets. Useful 
    when the data does not fit into memory (for both frequentist and Bayesian regression), 
    to make running time manageable (mainly for Bayesian regression), and to reduce 
    the total running time because of reduced or less severe memory-spillover into 
    the virtual memory. This is an implementation of Merge & Reduce for linear regression
    as described in Geppert, L.N., Ickstadt, K., Munteanu, A., & Sohler, C. (2020).
    'Streaming statistical models via Merge & Reduce'. International Journal of
    Data Science and Analytics, 1-17, <doi:10.1007/s41060-020-00226-0>.
	"""
	
	cran = "mrregression" 

	version("1.0.0", md5="91770e31b7c191b8ecdf4d9abb5b6144")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.5:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
