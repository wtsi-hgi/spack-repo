# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGd(RPackage):
	"""Geographical Detectors for Assessing Spatial Factors

	Geographical detectors for measuring spatial stratified heterogeneity,
             as described in Jinfeng Wang (2010) <doi:10.1080/13658810802443457> and 
             Jinfeng Wang (2016) <doi:10.1016/j.ecolind.2016.02.052>. Includes the
             optimal discretization of continuous data, four primary functions of 
             geographical detectors, comparison of size effects of spatial unit and 
             the visualizations of results. 
             To use the package and to refer the 
             descriptions of the package, methods and case datasets, please cite 
             Yongze Song (2020) <doi:10.1080/15481603.2020.1760434>.
             The model has been applied in factor exploration of road performance and 
             multi-scale spatial segmentation for network data, as described in 
             Yongze Song (2018) <doi:10.3390/rs10111696> and 
             Yongze Song (2020) <doi:10.1109/TITS.2020.3001193>, respectively. 
	"""
	
	cran = "GD" 

	version("10.3", md5="77c3ddb3db1016b17c606ebb84b89cf5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-bammtools", type=("build", "run"))
