# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultidimbio(RPackage):
	"""Multivariate Analysis and Visualization for Biological Data

	Code to support a systems biology research program from inception through publication.  The methods focus on dimension reduction approaches to detect patterns in complex, multivariate experimental data and places an emphasis on informative visualizations.  The goal for this project is to create a package that will evolve over time, thereby remaining relevant and reflective of current methods and techniques.  As a result, we encourage suggested additions to the package, both methodological and graphical.
	"""
	
	cran = "multiDimBio" 

	version("1.2.2", md5="98d45f2375ddc2acde6dc905e5a8ce9f")

	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-lme4@1.1.21:", type=("build", "run"))
	depends_on("r-pcamethods@1.76:", type=("build", "run"))
	depends_on("r-misc3d@0.8.4:", type=("build", "run"))
	depends_on("r-mass@7.3.29:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-gridgraphics@0.1.5:", type=("build", "run"))
