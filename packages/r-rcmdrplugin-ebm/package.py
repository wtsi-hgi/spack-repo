# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginEbm(RPackage):
	"""Rcmdr Evidence Based Medicine Plug-in Package

	Rcmdr plug-in GUI extension for Evidence Based Medicine medical indicators calculations (Sensitivity, specificity, absolute risk reduction, relative risk, ...).
	"""
	
	cran = "RcmdrPlugin.EBM" 

	version("1.0-10", md5="72b828237dc02ae1d434714f53526889")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcmdr@1.7:", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
