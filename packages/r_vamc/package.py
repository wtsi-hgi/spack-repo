# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVamc(RPackage):
	"""A Monte Carlo Valuation Framework for Variable Annuities

	Implementation of a Monte Carlo simulation engine for valuing synthetic portfolios of 
    variable annuities, which reflect realistic features of common annuity contracts in practice. 
    It aims to facilitate the development and dissemination of research related to the efficient 
    valuation of a portfolio of large variable annuities. The main valuation methodology was 
    proposed by Gan (2017) <doi:10.1515/demo-2017-0021>.
	"""
	
	cran = "vamc" 

	version("0.2.1", md5="0055e8b57d66a340a4441a1e16e72269")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rdpack@0.4:", type=("build", "run"))
