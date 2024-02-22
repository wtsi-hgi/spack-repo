# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatticedesign(RPackage):
	"""Lattice-Based Space-Filling Designs

	Lattice-based space-filling designs with fill or separation distance properties including
  interleaved lattice-based minimax distance designs proposed in Xu He (2017)
  <doi:10.1093/biomet/asx036>, interleaved lattice-based maximin distance designs proposed
  in Xu He (2018) <doi:10.1093/biomet/asy069>, (sliced) rotated sphere packing designs 
  proposed in Xu He (2017) <doi:10.1080/01621459.2016.1222289> and Xu He (2019) 
  <doi:10.1080/00401706.2018.1458655>, and densest packing-based maximum projections 
  designs proposed in Xu He (2020) <doi:10.1093/biomet/asaa057> and Xu He (2018) 
  <arXiv:1709.02062v2>. 
	"""
	
	cran = "LatticeDesign" 

	version("2.0-5", md5="2c5ac4185aa12b700d065b5f62a3227b")

