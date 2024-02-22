# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoasso(RPackage):
	"""Higher Order Assortativity for Complex Networks

	Allows to evaluate Higher Order Assortativity of complex networks defined through objects of class 'igraph' from the package of the same name. The package returns a result also for directed and weighted graphs. References, Arcagni, A., Grassi, R., Stefani, S., & Torriero, A. (2017) <doi:10.1016/j.ejor.2017.04.028> Arcagni, A., Grassi, R., Stefani, S., & Torriero, A. (2021) <doi:10.1016/j.jbusres.2019.10.008> Arcagni, A., Cerqueti, R., & Grassi, R. (2023) <doi:10.48550/arXiv.2304.01737>.
	"""
	
	cran = "HOasso" 

	version("1.0.1", md5="2766b5cd58c941f322bef6d2ad40c691")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
