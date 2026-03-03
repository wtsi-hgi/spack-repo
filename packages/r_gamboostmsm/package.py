# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamboostmsm(RPackage):
	"""Boosting Multistate Models

	Contains infrastructure for using mboost::gamboost() in order to estimate multistate models.
	"""
	
	cran = "gamboostMSM" 

	version("1.1.88", md5="6aa1bd2b97f28fd1676c2b3a98a13858")

	depends_on("r-mboost@2.2.2:", type=("build", "run"))
