# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSorptionanalysis(RPackage):
	"""Static Adsorption Experiment Plotting and Analysis

	Provides tools to efficiently analyze and visualize laboratory data from aqueous static adsorption experiments. The package provides functions to plot Langmuir, Freundlich, and Temkin isotherms and functions to determine the statistical conformity of data points to the Langmuir, Freundlich, and Temkin adsorption models through statistical characterization of the isothermic least squares regressions lines. Scientific Reference: Dada, A.O, Olalekan, A., Olatunya, A. (2012) <doi:10.9790/5736-0313845>.
	"""
	
	cran = "SorptionAnalysis" 

	version("0.1.0", md5="669cab7097cd674b2814d90a5fcc1818")

