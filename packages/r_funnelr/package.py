# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunnelr(RPackage):
	"""Funnel Plots for Proportion Data

	A set of simplified functions for creating funnel plots for proportion data. This package supports user defined benchmarks, confidence limits and estimation methods (i.e. exact or approximate) based on Spiegelhalter (2005) <doi:10.1002/sim.1970>. Additional routines for returning scored unit level data according to a set of specifications is also implemented for convenience. Specifically, both a categorical and a continuous score variable is returned to the sample data frame, which identifies which observations are deemed extreme or in control. Typically, such variables are useful as stratifications or covariates in further exploratory analyses. Lastly, the plotting routine returns a base funnel plot ('ggplot2'), which can also be tailored.
	"""
	
	homepage = "https://matt-kumar.shinyapps.io/funnel/"
	cran = "funnelR" 

	version("0.1.0", md5="95f31e52db0e7337a55fc88796b96105")

	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
