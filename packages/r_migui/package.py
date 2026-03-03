# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigui(RPackage):
	"""Graphical User Interface to the 'mi' Package

	This GUI for the mi package walks the user through the steps of multiple imputation and the analysis of completed data.
	"""
	
	cran = "migui" 

	version("1.3", md5="101b98081f8796394189adcbd5f36919")

	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-mi@1.1:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
