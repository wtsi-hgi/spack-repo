# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgos(RPackage):
	"""Automatic Regression for Governing Equations (ARGOS)

	Comprehensive set of tools for performing system identification of both linear and nonlinear dynamical systems directly from data. The Automatic Regression for Governing Equations (ARGOS) simplifies the complex task of constructing mathematical models of dynamical systems from observed input and output data, supporting various types of systems, including those described by ordinary differential equations. It employs optimal numerical derivatives for enhanced accuracy and employs formal variable selection techniques to help identify the most relevant variables, thereby enabling the development of predictive models for system behavior analysis.
	"""
	
	homepage = "<https://github.com/kevinegan31/ARGOS-Package>"
	cran = "ARGOS" 

	version("0.1.1", md5="17d2ec880da3dc8b5c9428a7ec262d90")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
