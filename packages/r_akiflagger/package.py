# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAkiflagger(RPackage):
	"""Flags Acute Kidney Injury (AKI)

	Flagger to detect acute kidney injury (AKI) in a patient dataset.
	"""
	
	homepage = "https://github.com/isaranwrap/akiFlagger"
	cran = "akiFlagger" 

	version("0.3.0", md5="d72c482e46fed3ab4dd83b67a2fde21e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
