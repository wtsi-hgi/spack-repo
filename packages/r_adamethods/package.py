# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdamethods(RPackage):
	"""Archetypoid Algorithms and Anomaly Detection

	Collection of several algorithms to obtain archetypoids with small and large databases, and with both classical 
	multivariate data and functional data (univariate and multivariate). Some of these algorithms also allow to detect 
	anomalies (outliers). Please see Vinue and Epifanio (2020) <doi:10.1007/s11634-020-00412-9>. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "adamethods" 

	version("1.2.1", md5="b9968656ed786b397288f2484c5e79f6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-anthropometry", type=("build", "run"))
	depends_on("r-archetypes", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-tolerance", type=("build", "run"))
	depends_on("r-univoutl", type=("build", "run"))
