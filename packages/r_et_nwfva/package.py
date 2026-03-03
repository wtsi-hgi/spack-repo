# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtNwfva(RPackage):
	"""Forest Yield Tables for Northwest Germany and their Application

	The new yield tables developed by the Northwest German Forest 
  Research Institute (NW-FVA) provide a forest management tool for the five 
  main commercial tree species oak, beech, spruce, Douglas-fir and pine for 
  northwestern Germany. The new method applied for deriving yield tables 
  combines measurements of growth and yield trials with growth simulations 
  using a state-of-the-art single-tree growth simulator. By doing so, the new 
  yield tables reflect the current increment level and the recommended 
  graduated thinning from above is the underlying management concept. The yield
  tables are provided along with methods for deriving the site index and for 
  interpolating between age and site indices and extrapolating beyond age and 
  site index ranges. The inter-/extrapolations are performed traditionally by 
  the rule of proportion or with a functional approach.
	"""
	
	homepage = "https://github.com/rnuske/et.nwfva"
	cran = "et.nwfva" 

	version("0.1.1", md5="37b2177d6168f5275d94c6377f22a678")

	depends_on("r@3.5:", type=("build", "run"))
