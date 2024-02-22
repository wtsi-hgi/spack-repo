# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeductive(RPackage):
	"""Data Correction and Imputation Using Deductive Methods

	Attempt to repair inconsistencies and missing values in
        data records by using information from valid values and
        validation rules restricting the data.
	"""
	
	homepage = "https://github.com/data-cleaning/deductive"
	cran = "deductive" 

	version("1.0.0", md5="95fb0e43dd522b8ed0f7705e9bc69bea")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lintools", type=("build", "run"))
	depends_on("r-validate", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
