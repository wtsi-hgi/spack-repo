# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataclass(RPackage):
	"""Easily Create Structured Lists or Data Frames with Input
Validation

	Easily define templates for lists and data frames that validate
    each element. Specify the expected type (i.e., character, numeric, etc),
    expected length, minimum and maximum values, allowable values, and more for
    each element in your data. Decide whether violations of these expectations
    should throw an error or a warning. This package is useful for validating
    data within R processes which pull from dynamic data sources such as
    databases and web APIs to provide an extra layer of validation around input
    and output data.
	"""
	
	cran = "dataclass" 

	version("0.3.0", md5="59f207908a9495cbd473b72a56a6cc43")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
