# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHts(RPackage):
	"""Hierarchical and Grouped Time Series

	Provides methods for analysing and forecasting hierarchical and 
    grouped time series. The available forecast methods include bottom-up,
    top-down, optimal combination reconciliation (Hyndman et al. 2011) 
    <doi:10.1016/j.csda.2011.03.006>, and trace minimization reconciliation
    (Wickramasuriya et al. 2018) <doi:10.1080/01621459.2018.1448825>.
	"""
	
	homepage = "https://pkg.earo.me/hts/"
	cran = "hts" 

	version("6.0.2", md5="04aa84f7fabad5b7d975c530161c0bd9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-forecast@8.12:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
