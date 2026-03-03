# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetect(RPackage):
	"""Analyzing Wildlife Data with Detection Error

	Models for analyzing site occupancy and count data models
  with detection error, including single-visit based models,
  conditional distance sampling and time-removal models.
  Package development was supported by the
  Alberta Biodiversity Monitoring Institute
  and the Boreal Avian Modelling Project.
	"""
	
	homepage = "https://github.com/psolymos/detect"
	cran = "detect" 

	version("0.4-6", md5="f90c9b1162d0e2bee27ac74d514d75c8")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
