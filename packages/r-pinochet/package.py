# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinochet(RPackage):
	"""Data About the Victims of the Pinochet Regime, 1973-1990

	Packages data about the victims of the Pinochet regime as compiled by the Chilean National Commission for Truth and Reconciliation Report (1991, ISBN:9780268016463).
	"""
	
	homepage = "http://github.com/danilofreire/pinochet"
	cran = "pinochet" 

	version("0.1.0", md5="9e2393bd6ca49ea0cc8b7ce3bd24fcd0")

	depends_on("r@3.5:", type=("build", "run"))
