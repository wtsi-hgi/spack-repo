# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsdesign(RPackage):
	"""Design, Planning and Analysis of Observational Studies

	A suite of functions for the design of case-control and two-phase studies, and the analysis of data that arise from them. Functions in this packages provides Monte Carlo based evaluation of operating characteristics such as powers for estimators of the components of a logistic regression model. For additional detail see: Haneuse S, Saegusa T and Lumley T (2011)<doi:10.18637/jss.v043.i11>.
	"""
	
	cran = "osDesign" 

	version("1.8", md5="4f31c8f0adeab8b00134b3148a0e9b04")

	depends_on("r@3.5:", type=("build", "run"))
