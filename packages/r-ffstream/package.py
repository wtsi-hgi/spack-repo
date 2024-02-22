# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfstream(RPackage):
	"""Forgetting Factor Methods for Change Detection in Streaming Data

	An implementation of the adaptive forgetting factor scheme described in Bodenham and Adams (2016) <doi:10.1007/s11222-016-9684-8> which adaptively estimates the mean and variance of a stream in order to detect multiple changepoints in streaming data. The implementation is in 'C++' and uses 'Rcpp'. Additionally, implementations of the fixed forgetting factor scheme from the same paper, as well as the classic cumulative sum ('CUSUM') and exponentially weighted moving average ('EWMA') methods, are included.
	"""
	
	cran = "ffstream" 

	version("0.1.7.2", md5="5b5e5374843f016d7dd878df13a432f7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
