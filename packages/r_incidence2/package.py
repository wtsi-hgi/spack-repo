# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncidence2(RPackage):
	"""Compute, Handle and Plot Incidence of Dated Events

	Provides functions and classes to compute, handle and visualise 
  incidence from dated events for a defined time interval. Dates can be 
  provided in various standard formats. The class 'incidence2' is used to store
  computed incidence and can be easily manipulated, subsetted, and plotted.
  This package is part of the RECON (<https://www.repidemicsconsortium.org/>) 
  toolkit for outbreak analysis (<https://www.reconverse.org>).
	"""
	
	homepage = "https://www.reconverse.org/incidence2/"
	cran = "incidence2" 

	version("2.2.3", md5="60029d0ac1b9b1e8b399526917a1ebff", url="https://cran.r-project.org/src/contrib/incidence2_2.2.3.tar.gz")

	depends_on("r-grates@1:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
