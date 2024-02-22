# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenguedatahub(RPackage):
	"""A Tidy Format Datasets of Dengue by Country

	Provides a weekly, monthly, yearly summary of dengue cases by state/ province/ country.
	"""
	
	homepage = "https://denguedatahub.netlify.app/"
	cran = "denguedatahub" 

	version("1.0.4", md5="d9dc7237e15ccf9f620b3e34f343915b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
