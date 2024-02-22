# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginRoc(RPackage):
	"""Rcmdr Receiver Operator Characteristic Plug-in Package

	Rcmdr GUI extension plug-in for Receiver Operator Characteristic tools from pROC package. Also it ads a Rcmdr GUI extension for Hosmer and Lemeshow GOF test from the package ResourceSelection.
	"""
	
	cran = "RcmdrPlugin.ROC" 

	version("1.0-19", md5="2b14deca67163578a8905b80ea60ed8a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcmdr@1.7:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-resourceselection", type=("build", "run"))
