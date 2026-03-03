# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErp(RPackage):
	"""Significance Analysis of Event-Related Potentials Data

	Functions for signal detection and identification designed for Event-Related Potentials (ERP) data in a linear model framework. The functional F-test proposed in Causeur, Sheu, Perthame, Rufini (2018, submitted) for analysis of variance issues in ERP designs is implemented for signal detection (tests for mean difference among groups of curves in One-way ANOVA designs for example). Once an experimental effect is declared significant, identification of significant intervals is achieved by the multiple testing procedures reviewed and compared in Sheu, Perthame, Lee and Causeur (2016, <DOI:10.1214/15-AOAS888>). Some of the methods gathered in the package are the classical FDR- and FWER-controlling procedures, also available using function p.adjust. The package also implements the Guthrie-Buchwald procedure (Guthrie and Buchwald, 1991 <DOI:10.1111/j.1469-8986.1991.tb00417.x>), which accounts for the auto-correlation among t-tests to control erroneous detection of short intervals. The Adaptive Factor-Adjustment method is an extension of the method described in Causeur, Chu, Hsieh and Sheu (2012, <DOI:10.3758/s13428-012-0230-0>). It assumes a factor model for the correlation among tests and combines adaptively the estimation of the signal and the updating of the dependence modelling (see Sheu et al., 2016, <DOI:10.1214/15-AOAS888> for further details).
	"""
	
	homepage = "http://erpinr.org"
	cran = "ERP" 

	version("2.2", md5="6df9178e18fde28093b9a32ab68d3dbd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
