# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidfieldr(RPackage):
	"""Tools and Methods for Working with MIDFIELD Data in 'R'

	Provides tools and demonstrates methods for working with individual 
  undergraduate student-level records (registrar's data) in 'R'. Tools include 
  filters for program codes, data sufficiency, and timely completion. Methods 
  include gathering blocs of records, computing quantitative metrics such as 
  graduation rate, and creating charts to visualize comparisons. 'midfieldr'  
  interacts with practice data provided in 'midfielddata', a data package with 
  an installed size of about 24 Mb available via a 'drat' repository. 
  Instructions at <https://midfieldr.github.io/midfielddata/>. This work is 
  supported by the US National Science Foundation through grant numbers 1545667 
  and 2142087.
	"""
	
	homepage = "https://midfieldr.github.io/midfieldr/"
	cran = "midfieldr" 

	version("1.0.1", md5="9c97a041f95887b114b0291316d44f46")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-wrapr", type=("build", "run"))
