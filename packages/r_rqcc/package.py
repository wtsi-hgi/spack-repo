# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqcc(RPackage):
	"""Robust Quality Control Chart

	Constructs various robust quality control charts based on the median or Hodges-Lehmann estimator (location) and the median absolute deviation (MAD) or Shamos estimator (scale). The estimators used for the robust control charts are all unbiased with a sample of finite size. For more details, see Park, Kim and Wang (2022) <doi:10.1080/03610918.2019.1699114>. In addition, using this R package, the conventional quality control charts such as X-bar, S, R, p, np, u, c, g, h, and t charts are also easily constructed. This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No. 2022R1A2C1091319).
	"""
	
	homepage = "https://AppliedStat.GitHub.io/R/"
	cran = "rQCC" 

	version("2.22.12", md5="2c941b886aee88934030887abad0eadc")

	depends_on("r@3.2.3:", type=("build", "run"))
