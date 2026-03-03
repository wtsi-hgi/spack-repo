# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersdx(RPackage):
	"""Personalized Diagnostics Rules for Subgroup Identification and
Personalized Biomarker Discovery

	Tailoring the optimal biomarker(s) for disease screening or diagnosis based on subjects' individual characteristics.
	"""
	
	cran = "persDx" 

	version("0.5.0", md5="7b2aaf7d7673d4f8f1277e064e760cde")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-survivalroc", type=("build", "run"))
