# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncidence(RPackage):
	"""Compute, Handle, Plot and Model Incidence of Dated Events

	Provides functions and classes to compute, handle and visualise
  incidence from dated events for a defined time interval. Dates can be provided
  in various standard formats. The class 'incidence' is used to store computed
  incidence and can be easily manipulated, subsetted, and plotted. In addition,
  log-linear models can be fitted to 'incidence' objects using 'fit'. This
  package is part of the RECON (<https://www.repidemicsconsortium.org/>) toolkit
  for outbreak analysis.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/incidence/"
	cran = "incidence" 

	version("1.7.3", md5="4e3d46c14dd29071bda7b7d2830595e4")

	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-aweek@0.2:", type=("build", "run"))
