# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTakos(RPackage):
	"""Analysis of Differential Calorimetry Scans

	It includes functions for applying methodologies utilized for single-process kinetic analysis of solid-state processes were recently summarized and described in the Recommendation of ICTAC Kinetic Committee. These methods work with the basic kinetic equation. The Methodologies included refers to  Avrami, Friedman, Kissinger, Ozawa, OFM, Mo, Starink, isoconversional methodology (Vyazovkin) according to ICATAC Kinetics Committee recommendations as reported in Vyazovkin S, Chrissafis K, Di Lorenzo ML, et al. ICTAC Kinetics Committee recommendations for collecting experimental thermal analysis data for kinetic computations. Thermochim Acta. 2014;590:1-23. <doi:10.1016/J.TCA.2014.05.036> .
	"""
	
	homepage = "https://github.com/sere3s/takos"
	cran = "takos" 

	version("0.2.0", md5="9bab64b4e2c4ca36eaa1311402c88434")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-smoother", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
