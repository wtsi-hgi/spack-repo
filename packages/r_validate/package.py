# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidate(RPackage):
	"""Data Validation Infrastructure

	Declare data validation rules and data quality indicators;
        confront data with them and analyze or visualize the results.
        The package supports rules that are per-field, in-record,
        cross-record or cross-dataset. Rules can be automatically
        analyzed for rule type and connectivity. Supports checks implied
        by an SDMX DSD file as well. See also Van der Loo
        and De Jonge (2018) <doi:10.1002/9781118897126>, Chapter 6
        and the JSS paper (2021) <doi:10.18637/jss.v097.i10>.
	"""
	
	homepage = "https://github.com/data-cleaning/validate"
	cran = "validate" 

	version("1.1.5", md5="c90a171a698be386cf85cb6bd09c30ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
