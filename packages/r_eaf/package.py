# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REaf(RPackage):
	"""Plots of the Empirical Attainment Function

	Computation and visualization of the empirical attainment function (EAF) for the analysis of random sets in multi-criterion optimization. M. López-Ibáñez, L. Paquete, and T. Stützle (2010) <doi:10.1007/978-3-642-02538-9_9>.
	"""
	
	homepage = "https://mlopez-ibanez.github.io/eaf/"
	cran = "eaf" 

	version("2.5", md5="b5a0c19ffe372c7be4d4677305a71f5e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
