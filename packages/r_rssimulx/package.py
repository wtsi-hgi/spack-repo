# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssimulx(RPackage):
	"""Extension of 'lixoftConnectors' for 'Simulx'

	Provides useful tools which supplement the use of 'Simulx' software and 'R' connectors ('Monolix Suite'). 'Simulx' is an easy, efficient and flexible application for clinical trial simulations. You need 'Simulx' software to be installed in order to use 'RsSimulx' package. Among others tasks, 'RsSimulx' provides the same functions as package 'mlxR' does with a compatibility with 'Simulx' software.
	"""
	
	cran = "RsSimulx" 

	version("2023.1", md5="67bf07431f63d6270c9a8bcaf0bbb227")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
