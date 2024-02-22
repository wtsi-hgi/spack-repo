# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremerisks(RPackage):
	"""Extreme Risk Measures

	A set of procedures for estimating risks related to extreme events via risk measures such as Expectile, Value-at-Risk, etc. is provided. Estimation methods for univariate independent observations and temporal dependent observations are available. The methodology is extended to the case of independent multidimensional observations.  The statistical inference is performed through parametric and non-parametric estimators. Inferential procedures such as confidence intervals, confidence regions and hypothesis testing are obtained by exploiting the asymptotic theory. Adapts the methodologies derived in Padoan and Stupfler (2020) <arxiv:2004.04078>, Padoan and Stupfler (2020) <arxiv:2007.08944>, Daouia et al. (2018) <doi:10.1111/rssb.12254>, Drees (2000) <doi:10.1214/aoap/1019487617>, Drees (2003) <doi:10.3150/bj/1066223272>, de Haan and Ferreira (2006) <doi:10.1007/0-387-34471-3>, de Haan et al. (2016) <doi:10.1007/s00780-015-0287-6>.
	"""
	
	homepage = "mypage.unibocconi.it/simonepadoan/"
	cran = "ExtremeRisks" 

	version("0.0.4", md5="158a6ee7425b6e8101c20b05cf83926f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
