# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsfun(RPackage):
	"""Integrative Dimension Reduction Analysis for Multi-Source Data

	The implement of integrative analysis methods based on a two-part penalization, which realizes dimension reduction analysis and mining the heterogeneity and association of multiple studies with compatible designs. The software package provides the integrative analysis methods including integrative sparse principal component analysis (Fang et al., 2018), integrative sparse partial least squares (Liang et al., 2021) and integrative sparse canonical correlation analysis, as well as corresponding individual analysis and meta-analysis versions. References: (1) Fang, K., Fan, X., Zhang, Q., and Ma, S. (2018). Integrative sparse principal component analysis. Journal of Multivariate Analysis, <doi:10.1016/j.jmva.2018.02.002>. (2) Liang, W., Ma, S., Zhang, Q., and Zhu, T. (2021). Integrative sparse partial least squares. Statistics in Medicine, <doi:10.1002/sim.8900>.
	"""
	
	cran = "iSFun" 

	version("1.1.0", md5="2235a19e4f6db1289020cd4a4c4782bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
