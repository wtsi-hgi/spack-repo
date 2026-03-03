# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrmplot(RPackage):
	"""Advanced Plotting of Ordinal Regression Models

	An extension to the Regression Modeling Strategies package that
    facilitates plotting ordinal regression  model predictions together with
    confidence intervals for each dependent variable level. 
    It also adds a functionality to plot the  model summary as a modifiable 
    object.
	"""
	
	homepage = "https://doi.org/10.1186/s12889-019-8072-7"
	cran = "ormPlot" 

	version("0.3.6", md5="a0a0b69a55a60eb8a2fcb954bc4f03bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rms@5.1.3:", type=("build", "run"))
	depends_on("r-gtable@0.3:", type=("build", "run"))
