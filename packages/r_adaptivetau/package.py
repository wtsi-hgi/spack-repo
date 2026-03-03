# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptivetau(RPackage):
	"""Tau-Leaping Stochastic Simulation

	Implements adaptive tau leaping to approximate the
        trajectory of a continuous-time stochastic process as
        described by Cao et al. (2007) The Journal of Chemical Physics
        <doi:10.1063/1.2745299> (aka. the Gillespie stochastic
        simulation algorithm).  This package is based upon work
        supported by NSF DBI-0906041 and NIH K99-GM104158 to Philip
        Johnson and NIH R01-AI049334 to Rustom Antia.
	"""
	
	cran = "adaptivetau" 

	version("2.3", md5="544cb5bb81e0f43ca0dcd62f0cdc6ebc")

	depends_on("r@2.10.1:", type=("build", "run"))
