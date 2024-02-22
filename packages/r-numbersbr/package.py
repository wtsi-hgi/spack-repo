# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumbersbr(RPackage):
	"""Validate, Compare and Format Identification Numbers from Brazil

	Validate, format and compare identification numbers used in Brazil.
  These numbers are used to identify individuals (CPF), vehicles (RENAVAN),
  companies (CNPJ) and etc.
  Functions to format, validate and compare these numbers have been 
  implemented in a vectorized way in order to speed up
  validations and comparisons in big datasets.
	"""
	
	cran = "numbersBR" 

	version("0.0.2", md5="257a507b4a96f3497339a8589fb08972")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
