# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRm2006(RPackage):
	"""RiskMetrics 2006 Methodology

	Estimation of the conditional covariance matrix using the RiskMetrics 2006 methodology of Zumbach (2007) <doi:10.2139/ssrn.1420185>.
	"""
	
	cran = "RM2006" 

	version("0.1.1", md5="7875adc2fc1f8327c2389a0affb789c8", url="https://cran.r-project.org/src/contrib/RM2006_0.1.1.tar.gz")

