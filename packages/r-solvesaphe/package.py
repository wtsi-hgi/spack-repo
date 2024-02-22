# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolvesaphe(RPackage):
	"""Solver Suite for Alkalinity-PH Equations

	Universal and robust algorithm for solving the total alkalinity-pH equation presented in G. Munhoven (2013) <doi:10.5194/gmd-6-1367-2013> and G. Munhoven (2021) <doi:10.5194/gmd-2020-447>. The total alkalinity-pH equation relates total alkalinity and pH for a given set of acid-base concentrations in a given water sample, among which carbonic acid. This package is particularly useful in marine chemistry involving dissolved inorganic carbon. Original package in Fortran can be found at <doi:10.5281/zenodo.4328965>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=SolveSAPHE"
	cran = "SolveSAPHE" 

	version("2.1.0", md5="5694b0507ce0760f891cb9c0366fd7cc")

	depends_on("r@2.10:", type=("build", "run"))
