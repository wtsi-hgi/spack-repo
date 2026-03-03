# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivregbls(RPackage):
	"""Tolerance Interval and EIV Regression - Method Comparison
Studies

	Assess the agreement in method comparison studies by tolerance intervals and errors-in-variables (EIV) regressions. The Ordinary Least Square regressions (OLSv and OLSh), the Deming Regression (DR), and the (Correlated)-Bivariate Least Square regressions (BLS and CBLS) can be used with unreplicated or replicated data. The BLS() and CBLS() are the two main functions to estimate a regression line, while XY.plot() and MD.plot() are the two main graphical functions to display, respectively an (X,Y) plot or (M,D) plot with the BLS or CBLS results. Four hyperbolic statistical intervals are provided: the Confidence Interval (CI), the Confidence Bands (CB), the Prediction Interval and the Generalized prediction Interval. Assuming no proportional bias, the (M,D) plot (Band-Altman plot) may be simplified by calculating univariate tolerance intervals (beta-expectation (type I) or beta-gamma content (type II)). Major updates from last version 1.0.0 are: title shortened, include the new functions BLS.fit() and CBLS.fit() as shortcut of the, respectively, functions BLS() and CBLS(). References: B.G. Francq, B. Govaerts (2016) <doi:10.1002/sim.6872>, B.G. Francq, B. Govaerts (2014) <doi:10.1016/j.chemolab.2014.03.006>, B.G. Francq, B. Govaerts (2014) <http://publications-sfds.fr/index.php/J-SFdS/article/view/262>, B.G. Francq (2013), PhD Thesis, UCLouvain, Errors-in-variables regressions to assess equivalence in method comparison studies, <https://dial.uclouvain.be/pr/boreal/object/boreal%3A135862/datastream/PDF_01/view>.
	"""
	
	cran = "BivRegBLS" 

	version("1.1.1", md5="19c28404d92488c784229e1a38a7bfb3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
