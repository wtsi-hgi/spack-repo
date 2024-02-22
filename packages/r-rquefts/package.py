# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRquefts(RPackage):
	"""Quantitative Evaluation of the Native Fertility of Tropical
Soils

	An implementation of the QUEFTS (Quantitative Evaluation of the Native Fertility of Tropical Soils) model. The model (1) estimates native nutrient (N, P, K) supply of soils from a few soil chemical properties; and (2) computes crop yield given that supply, crop parameters, fertilizer application, and crop attainable yield. See Janssen et al. (1990) <doi:10.1016/0016-7061(90)90021-Z> for the technical details and Sattari et al. (2014) <doi:10.1016/j.fcr.2013.12.005> for a recent evaluation and improvements.
	"""
	
	homepage = "https://CRAN.R-project.org/package=Rquefts"
	cran = "Rquefts" 

	version("1.2-3", md5="5e98bbdf12b85b94dd6d45039c76bcb1")

	depends_on("r-meteor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
