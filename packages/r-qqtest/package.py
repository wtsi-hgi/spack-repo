# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqtest(RPackage):
	"""Self Calibrating Quantile-Quantile Plots for Visual Testing

	Provides the function qqtest which incorporates uncertainty in its
    qqplot display(s) so that the user might have a better sense of the
    evidence against the specified distributional hypothesis.  qqtest draws a
    quantile quantile plot for visually assessing whether the data come from a
    test distribution that has been defined in one of many ways.  The vertical
    axis plots the data quantiles, the horizontal those of a test distribution.
    The default behaviour generates 1000 samples from the test distribution and
    overlays the plot with shaded pointwise interval estimates for the ordered
    quantiles from the test distribution.  A small number of independently
    generated exemplar quantile plots can also be overlaid.  Both the interval
    estimates and the exemplars provide different comparative information to
    assess the evidence provided by the qqplot for or against the hypothesis
    that the data come from the test distribution (default is normal or
    gaussian).  Finally, a visual test of significance (a lineup plot) can also
    be displayed to test the null hypothesis that the data come from the test
    distribution.
	"""
	
	homepage = "https://github.com/rwoldford/qqtest"
	cran = "qqtest" 

	version("1.2.0", md5="bff2021f3dc3eeed3c57958252358715")

	depends_on("r@2.10:", type=("build", "run"))
