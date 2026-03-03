# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirgr(RPackage):
	"""Suite of GR Hydrological Models for Precipitation-Runoff
Modelling

	Hydrological modelling tools developed at INRAE-Antony (HYCAR Research Unit, France). The package includes several conceptual rainfall-runoff models (GR4H, GR5H, GR4J, GR5J, GR6J, GR2M, GR1A) that can be applied either on a lumped or semi-distributed way. A snow accumulation and melt model (CemaNeige) and the associated functions for the calibration and evaluation of models are also included. Use help(airGR) for package description and references.
	"""
	
	homepage = "https://hydrogr.github.io/airGR/"
	cran = "airGR" 

	version("1.7.6", md5="91f1e03ae13f46e13101ce5f93fa0b59")

	depends_on("r@3.1:", type=("build", "run"))
