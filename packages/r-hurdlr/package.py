# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHurdlr(RPackage):
	"""Zero-Inflated and Hurdle Modelling Using Bayesian Inference

	When considering count data, it is often the case that many more zero counts than would be expected of some given distribution are observed. It is well established that data such as this can be reliably modelled using zero-inflated or hurdle distributions, both of which may be applied using the functions in this package. Bayesian analysis methods are used to best model problematic count data that cannot be fit to any typical distribution. The package functions are flexible and versatile, and can be applied to varying count distributions, parameter estimation with or without explanatory variable information, and are able to allow for multiple hurdles as it is also not uncommon that count data have an abundance of large-number observations which would be considered outliers of the typical distribution. In lieu of throwing out data or misspecifying the typical distribution, these extreme observations can be applied to a second, extreme distribution. With the given functions of this package, such a two-hurdle model may be easily specified in order to best manage data that is both zero-inflated and over-dispersed.
	"""
	
	cran = "hurdlr" 

	version("0.1", md5="8df3d28806063671ee779c0285e98551")

	depends_on("r@3.3:", type=("build", "run"))
