# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblepp(RPackage):
	"""Ensemble Postprocessing Data Sets

	Data sets for the chapter "Ensemble Postprocessing with R" of the book Stephane Vannitsem, Daniel S. Wilks, and Jakob W. Messner (2018) "Statistical Postprocessing of Ensemble Forecasts", Elsevier, 362pp. These data sets contain temperature and precipitation ensemble weather forecasts and corresponding observations at Innsbruck/Austria. Additionally, a demo with the full code of the book chapter is provided.
	"""
	
	cran = "ensemblepp" 

	version("1.0-0", md5="42eaa6d3e9f3416b8d2dd20a6221b46b")

	depends_on("r@2.10:", type=("build", "run"))
