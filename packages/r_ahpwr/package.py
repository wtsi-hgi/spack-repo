# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhpwr(RPackage):
	"""Compute Analytic Hierarchy Process

	Compute a tree level hierarchy, judgment matrix, consistency index and ratio, priority vectors, hierarchic synthesis and rank. Based on the book entitled "Models, Methods, Concepts and Applications of the Analytic Hierarchy Process" by Saaty and Vargas (2012, ISBN 978-1-4614-3597-6).
	"""
	
	cran = "AHPWR" 

	version("0.1.0", md5="85d54fcb6c230b0d8cceb05c3d293fe1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
