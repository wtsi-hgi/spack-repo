# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRafalib(RPackage):
	"""Convenience Functions for Routine Data Exploration

	A series of shortcuts for routine tasks originally developed by Rafael A. Irizarry to facilitate data exploration. 
	"""
	
	cran = "rafalib" 

	version("1.0.0", md5="3ec2db844e21fa6b6ac29dc46d739a37")

	depends_on("r-rcolorbrewer", type=("build", "run"))
