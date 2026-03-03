# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatseyes(RPackage):
	"""Create Catseye Plots Illustrating the Normal Distribution of the
Means

	Provides the tools to produce catseye plots, principally
    by catseyesplot() function which calls R's standard plot() function internally, or alternatively
    by the catseyes() function to overlay the catseye plot onto an existing
    R plot window. Catseye plots illustrate the normal distribution of the mean (picture a 
    normal bell curve reflected over its base and rotated 90 degrees), with a shaded confidence
    interval; they are an intuitive way of illustrating and comparing normally distributed estimates,
    and are arguably a superior alternative to standard confidence intervals, since they show the full
    distribution rather than fixed quantile bounds. The catseyesplot and catseyes functions require
    pre-calculated means and standard errors (or standard deviations), provided as numeric vectors;
    this allows the flexibility of obtaining this information from a variety of sources, such as
    direct calculation or prediction from a model.  Catseye plots, as illustrations of the
    normal distribution of the means, are described in Cumming (2013 & 2014).
    Cumming, G. (2013). The new statistics: Why and how. Psychological Science, 27, 7-29. <doi:10.1177/0956797613504966> pmid:24220629.
	"""
	
	cran = "catseyes" 

	version("0.2.5", md5="3afd053ea310ab126a0c7622a849f41d")

