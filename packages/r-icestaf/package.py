# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcestaf(RPackage):
	"""Functions to Support the ICES Transparent Assessment Framework

	Functions to support the ICES Transparent Assessment Framework
  <https://taf.ices.dk> to organize data, methods, and results used in ICES
  assessments. ICES is an organization facilitating international collaboration
  in marine science.
	"""
	
	homepage = "https://taf.ices.dk"
	cran = "icesTAF" 

	version("4.2.0", md5="336fa2ceeb064e6a443e3a65e8a2a5a4")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-taf@4.2:", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
