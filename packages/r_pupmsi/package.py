# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupmsi(RPackage):
	"""Moisture Sorption Isotherm Modeling Program

	Contains sixteen moisture sorption isotherm models, which evaluate the fitness of adsorption and desorption curves for further understanding of the relationship between moisture content and water activity. Fitness evaluation is conducted through parameter estimation and error analysis. Moreover, graphical representation, hysteresis area estimation, and isotherm classification through the equation of Blahovec & Yanniotis (2009) <doi:10.1016/j.jfoodeng.2008.08.007> which is based on the classification system introduced by Brunauer et. al. (1940) <doi:10.1021/ja01864a025> are also included for the visualization of models and hysteresis.
	"""
	
	cran = "PUPMSI" 

	version("0.1.0", md5="e72e61b6711dda4c8685517fd2c2cb86")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
