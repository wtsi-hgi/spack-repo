# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsec(RPackage):
	"""Partial Orders in Socio-Economics

	Implements tools for the analysis of partially ordered data, with a particular focus on the evaluation of multidimensional systems of indicators and on the analysis of poverty. References, Fattore M. (2016) <doi:10.1007/s11205-015-1059-6> Fattore M., Arcagni A. (2016) <doi:10.1007/s11205-016-1501-4> Arcagni A. (2017) <doi:10.1007/978-3-319-45421-4_19>.
	"""
	
	cran = "parsec" 

	version("1.2.7", md5="790048f026c862b15c6e5ef2c5ff8197")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-netrankr", type=("build", "run"))
