# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKstio(RPackage):
	"""Knowledge Space Theory Input/Output

	Knowledge space theory by Doignon and Falmagne (1999) 
   <doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical
   framework which proposes mathematical formalisms to operationalize 
   knowledge structures in a particular domain.  The 'kstIO' package 
   provides basic functionalities to read and write KST data from/to 
   files to be used together with the 'kst', 'kstMatrix', 'pks' or 
   'DAKS' packages.
	"""
	
	cran = "kstIO" 

	version("0.4-0", md5="4f29a62e6fb72dae9b87d91bc579b0e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pks@0.4.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-relations", type=("build", "run"))
	depends_on("r-kstmatrix", type=("build", "run"))
