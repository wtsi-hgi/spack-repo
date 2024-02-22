# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargeted(RPackage):
	"""Targeted Inference

	Various methods for targeted and semiparametric inference including
	     augmented inverse probability weighted (AIPW) estimators for missing data and
	     causal inference (Bang and Robins (2005) <doi:10.1111/j.1541-0420.2005.00377.x>),
         variable importance and conditional average treatment effects (CATE)
         (van der Laan (2006) <doi:10.2202/1557-4679.1008>),
	     estimators for risk differences and relative risks (Richardson et al. (2017)
	     <doi:10.1080/01621459.2016.1192546>), assumption lean inference for generalized
         linear model parameters (Vansteelandt et al. (2022) <doi:10.1111/rssb.12504>).
	"""
	
	cran = "targeted" 

	version("0.5", md5="537c663bc425f485ecf75c98d9ed0732")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lava@1.7:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-mets", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
