# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrs(RPackage):
	"""Categorical Regression Splines

	Regression splines that handle a mix of continuous and categorical (discrete) data often encountered in applied settings. I would like to gratefully acknowledge support from the Natural Sciences and Engineering Research Council of Canada (NSERC, <https://www.nserc-crsng.gc.ca>), the Social Sciences and Humanities Research Council of Canada (SSHRC, <https://www.sshrc-crsh.gc.ca>), and the Shared Hierarchical Academic Research Computing Network (SHARCNET, <https://www.sharcnet.ca>). We would also like to acknowledge the contributions of the GNU GSL authors. In particular, we adapt the GNU GSL B-spline routine gsl_bspline.c adding automated support for quantile knots (in addition to uniform knots), providing missing functionality for derivatives, and for extending the splines beyond their endpoints.
	"""
	
	homepage = "https://github.com/JeffreyRacine/R-Package-crs"
	cran = "crs" 

	version("0.15-37", md5="877e64da989db2f6341f3e297f9eccc3")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
