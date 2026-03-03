# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtransferentropy(RPackage):
	"""Measuring Information Flow Between Time Series with Shannon and
Renyi Transfer Entropy

	Measuring information flow between time series with Shannon and Rényi transfer entropy. See also Dimpfl and Peter (2013) <doi:10.1515/snde-2012-0044> and Dimpfl and Peter (2014) <doi:10.1016/j.intfin.2014.03.004> for theory and applications to financial time series. Additional references can be found in the theory part of the vignette.
	"""
	
	homepage = "https://github.com/BZPaper/RTransferEntropy"
	cran = "RTransferEntropy" 

	version("0.2.21", md5="0e847116092467425f1a9aae247e8613")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-future@1.19:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
