# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegperiod(RPackage):
	"""Determine Thermal Vegetation Periods

	Collection of common methods to determine growing season length in
  a simple manner. Start and end dates of the vegetation periods are calculated
  solely based on daily mean temperatures and the day of the year.
	"""
	
	homepage = "https://rnuske.github.io/vegperiod/"
	cran = "vegperiod" 

	version("0.4.0", md5="2518c110c960501d64c69a2490f872f7")

	depends_on("r@3.2:", type=("build", "run"))
