# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGldreg(RPackage):
	"""Fit GLD Regression/Quantile/AFT Model to Data

	Owing to the rich shapes of Generalised Lambda Distributions (GLDs), GLD standard/quantile/Accelerated Failure Time (AFT) regression is a competitive flexible model compared to standard/quantile/AFT regression. The proposed method has some major advantages: 1) it provides a reference line which is very robust to outliers with the attractive property of zero mean residuals and 2) it gives a unified, elegant quantile regression model from the reference line with smooth regression coefficients across different quantiles. For AFT model, it also eliminates the needs to try several different AFT models, owing to the flexible shapes of GLD. The goodness of fit of  the proposed model can be assessed via QQ plots and Kolmogorov-Smirnov tests and data driven smooth test, to ensure the appropriateness of the statistical inference under consideration. Statistical distributions of coefficients of the GLD regression line are obtained using simulation, and interval estimates are obtained directly from simulated data.  References include the following: Su (2015) "Flexible Parametric Quantile Regression Model" <doi:10.1007/s11222-014-9457-1>, Su (2021) "Flexible parametric accelerated failure time model"<doi:10.1080/10543406.2021.1934854>.
	"""
	
	cran = "GLDreg" 

	version("1.1.1", md5="4313131c5ec8f3da197e9b0a177e8a6a")

	depends_on("r-gldex@2.0.0.5:", type=("build", "run"))
	depends_on("r-ddst", type=("build", "run"))
