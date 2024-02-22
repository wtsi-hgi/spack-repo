# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgc(RPackage):
	"""Koeppen-Geiger Climatic Zones

	Aids in identifying the Koeppen-Geiger (KG) climatic zone for 
    a given location. The Koeppen-Geiger climate zones were first published in 1884, as a system
    to classify regions of the earth by their relative heat and humidity through the year, for 
    the benefit of human health, plant and agriculture and other human activity [1]. This climate
    zone classification system, applicable to all of the earths surface, has continued to be 
    developed by scientists up to the present day.  Recently one of use (FZ) has published updated,
    higher accuracy KG climate zone definitions [2]. In this package we use these updated 
    high-resolution maps as the data source [3]. We provide functions that return the KG climate zone 
    for a given longitude and lattitude, or for a given United States zip code. In addition
    the CZUncertainty() function will check climate zones nearby to check if the given location
    is near a climate zone boundary. In addition an interactive shiny app is provided to define 
    the KG climate zone for a given longitude and lattitude, or United States zip code. 
    Digital data, as well as animated maps, showing the shift of the climate zones are provided 
    on the following website <http://koeppen-geiger.vu-wien.ac.at>.
    This work was supported by the DOE-EERE SunShot award DE-EE-0007140.
     [1] W. Koeppen, (2011) <doi:10.1127/0941-2948/2011/105>.
     [2] F. Rubel and M. Kottek, (2010) <doi:10.1127/0941-2948/2010/0430>.
     [3] F. Rubel, K. Brugger, K. Haslinger, and I. Auer, (2016) <doi:10.1127/metz/2016/0816>.
	"""
	
	cran = "kgc" 

	version("1.0.0.2", md5="34f07a0ce3fcb732848b4b498916cce0")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
