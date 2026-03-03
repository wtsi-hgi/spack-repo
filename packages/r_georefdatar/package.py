# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeorefdatar(RPackage):
	"""Geosciences Reference Datasets

	Reference datasets commonly used in the geosciences. These include 
  standard atomic weights of the elements, a periodic table, a list of minerals 
  including their abbreviations and chemistry, geochemical data of reservoirs 
  (primitive mantle, continental crust, mantle, basalts, etc.), decay constants 
  and isotopic ratios frequently used in geochronology, color codes of the 
  chronostratigraphic chart. In addition, the package provides functions for 
  basic queries of atomic weights, the list of minerals, and chronostratigraphic
  chart colors. All datasets are fully referenced, and a BibTeX file containing 
  the references is included.
	"""
	
	homepage = "https://github.com/abuseki/georefdatar"
	cran = "georefdatar" 

	version("0.6.5", md5="654788e628930230491bdca5d5eec487")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
