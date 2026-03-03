# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlgdata(RPackage):
	"""Datasets for Use with Salvan, Sartori and Pace (2020)

	Contains the datasets for use with the book Salvan, Sartori and Pace (2020, ISBN:978-88-470-4002-1) "Modelli Lineari Generalizzati".
	"""
	
	cran = "MLGdata" 

	version("0.1.0", md5="c7b8f0e9a923916f928c7aafebeffe9d")

	depends_on("r@3.5:", type=("build", "run"))
