# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlone(RPackage):
	"""Datasets from the Survival TV Series Alone

	A collection of datasets on the Alone survival TV series in tidy format. 
  Included in the package are 4 datasets detailing the survivors, their loadouts,
  episode details and season information.
	"""
	
	homepage = "https://github.com/doehm/alone"
	cran = "alone" 

	version("0.3", md5="d37f19534f68fa697ee478b6840e42ea")

	depends_on("r@3.5:", type=("build", "run"))
