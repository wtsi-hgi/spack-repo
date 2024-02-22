# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKst(RPackage):
	"""Knowledge Space Theory

	Knowledge space theory by Doignon and Falmagne (1999) 
   <doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical
   framework, which proposes mathematical formalisms to operationalize 
   knowledge structures in a particular domain. The 'kst' package provides 
   basic functionalities to generate, handle, and manipulate knowledge 
   structures and knowledge spaces.
	"""
	
	homepage = "https://homepage.uni-graz.at/en/cord.hockemeyer/"
	cran = "kst" 

	version("0.5-4", md5="349a92f3d494e430ba5fcc61ac115724")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-relations@0.6.7:", type=("build", "run"))
	depends_on("r-sets@1.0.17:", type=("build", "run"))
