# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGauser(RPackage):
	"""Lotka-Volterra Models for Gause's 'Struggle for Existence'

	A collection of tools and data for analyzing the Gause microcosm experiments, and for fitting Lotka-Volterra models to time series data. Includes methods for fitting single-species logistic growth, and multi-species interaction models, e.g. of competition, predator/prey relationships, or mutualism. See documentation for individual functions for examples. In general, see the lv_optim() function for examples of how to fit parameter values in multi-species systems. Note that the general methods applied here, as well as the form of the differential equations that we use, are described in detail in the Quantitative Ecology textbook by Lehman et al., available at <http://hdl.handle.net/11299/204551>, and in Lina K. Mühlbauer, Maximilienne Schulze, W. Stanley Harpole, and Adam T. Clark. 'gauseR': Simple methods for fitting Lotka-Volterra models describing Gause's 'Struggle for Existence' in the journal Ecology and Evolution.
	"""
	
	cran = "gauseR" 

	version("1.2", md5="90e17e71bdbab1b4ac08a8477f8cbbbc")

	depends_on("r-desolve", type=("build", "run"))
