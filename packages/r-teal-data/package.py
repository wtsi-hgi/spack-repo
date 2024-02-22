# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealData(RPackage):
	"""Data Model for 'teal' Applications

	Provides a 'teal_data' class as a unified data model for
    'teal' applications focusing on reproducibility and relational data.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.data/"
	cran = "teal.data" 

	version("0.5.0", md5="27df9defb100298c90ed99538fd02a8c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-teal-code@0.5:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
