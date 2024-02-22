# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddt(RPackage):
	"""Analysis of Accelerated Destructive Degradation Test Data

	Accelerated destructive degradation tests (ADDT) are often used to collect necessary data for assessing the long-term properties of polymeric materials. Based on the collected data, a thermal index (TI) is estimated. The TI can be useful for material rating and comparison. This package implements the traditional method based on the least-squares method, the parametric method based on maximum likelihood estimation, and the semiparametric method based on spline methods, and the corresponding methods for estimating TI for polymeric materials. The traditional approach is a two-step approach that is currently used in industrial standards, while the parametric method is widely used in the statistical literature. The semiparametric method is newly developed. Both the parametric and semiparametric approaches allow one to do statistical inference such as quantifying uncertainties in estimation, hypothesis testing, and predictions. Publicly available datasets are provided illustrations. More details can be found in Jin et al. (2017).
	"""
	
	cran = "ADDT" 

	version("2.0", md5="12abdfde04418a86c1a6c65d4d5235c6")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
