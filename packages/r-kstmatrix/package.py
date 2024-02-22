# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKstmatrix(RPackage):
	"""Basic Functions in Knowledge Space Theory Using Matrix
Representation

	Knowledge space theory by Doignon and Falmagne (1999)
   <doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical
   framework, which proposes mathematical formalisms to operationalize
   knowledge structures in a particular domain. The 'kstMatrix' package 
   provides basic functionalities to generate, handle, and manipulate 
   knowledge structures and knowledge spaces. Opposed to the 'kst'
   package, 'kstMatrix' uses matrix representations for knowledge
   structures. Furthermore, 'kstMatrix' contains several knowledge spaces
   developed by the research group around Cornelia Dowling through
   querying experts.
	"""
	
	cran = "kstMatrix" 

	version("0.2-0", md5="b80704d012c68a267fb2e0d3b0391105")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-pks", type=("build", "run"))
