# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQi(RPackage):
	"""Quantity-Intensity Relationship of Soil Potassium

	The quantity-intensity (Q/I) relationships, first introduced by Beckett
  (1964), can be employed to assess the K supplying capacity of different soils 
  based on solid-solution exchange equilibria. Such relationships describe the 
  changes in K+ concentration in the soil solution (or the intensity factor) in 
  relation to the corresponding changes in K+ at exchange sites of the soil 
  (or the capacity or quantity factor). Activity ratio of K to Ca or Ca+Mg 
  is generally used as the variable denoting the intensity, whereas, change 
  in exchangeable K is used to denote the quantity factor. 
	"""
	
	cran = "QI" 

	version("0.1.0", md5="9b8f6f97d9fd4cb862658b4f96b40125")

	depends_on("r-ggplot2", type=("build", "run"))
