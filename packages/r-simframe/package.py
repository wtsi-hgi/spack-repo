# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimframe(RPackage):
	"""Simulation Framework

	A general framework for statistical simulation, which allows researchers to make use of a wide range of simulation designs with minimal programming effort.  The package provides functionality for drawing samples from a distribution or a finite population, for adding outliers and missing values, as well as for visualization of the simulation results.  It follows a clear object-oriented design and supports parallel computing to increase computational performance.
	"""
	
	cran = "simFrame" 

	version("0.5.4", md5="1b945fc88f16a324a6741b9ab00daf4a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
