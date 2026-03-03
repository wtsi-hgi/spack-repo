# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REms(RPackage):
	"""Epimed Solutions Collection for Data Editing, Analysis, and
Benchmark of Health Units

	Collection of functions related to benchmark with prediction models
	 for data analysis and editing of clinical and epidemiological data.
	"""
	
	cran = "ems" 

	version("1.3.11", md5="106f1e2fe1f692920914ca57bdd36db7")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
