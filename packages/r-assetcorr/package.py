# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssetcorr(RPackage):
	"""Estimating Asset Correlations from Default Data

	Functions for the estimation of intra- and inter-cohort correlations in the Vasicek credit portfolio model. For intra-cohort correlations, the package covers the two method of moments estimators of Gordy (2000) <doi:10.1016/S0378-4266(99)00054-0>, the method of moments estimator of Lucas (1995) <https://jfi.pm-research.com/content/4/4/76> and a Binomial approximation extension of this approach. Moreover, the maximum likelihood estimators of Gordy and Heitfield (2010) <http://elsa.berkeley.edu/~mcfadden/e242_f03/heitfield.pdf> and Duellmann and Gehde-Trapp (2004) <http://hdl.handle.net/10419/19729> are implemented. For inter-cohort correlations, the method of moments estimator of Bluhm and Overbeck (2003) <doi:10.1007/978-3-642-59365-9_2>/Bams et al. (2016) <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2676595> is provided and the maximum likelihood estimators comprise the approaches of Gordy and Heitfield (2010)/Kalkbrener and Onwunta (2010) <ISBN: 978-1906348250> and Pfeuffer et al. (2020). Bootstrap and Jackknife procedures for bias correction are included as well as the method of moments estimator of Frei and Wunsch (2018) <doi:10.21314/JCR.2017.231> for auto-correlated time series.
	"""
	
	cran = "AssetCorr" 

	version("1.0.4", md5="baaf3e7bd391035644d62a28dbc5e0c1")

	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mvquad", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
