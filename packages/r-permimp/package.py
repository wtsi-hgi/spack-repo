# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermimp(RPackage):
	"""Conditional Permutation Importance

	An add-on to the 'party' package, with a faster implementation 
   of the partial-conditional permutation importance for random forests. The 
   standard permutation importance is implemented exactly the same as in 
   the 'party' package. The conditional permutation importance can be 
   computed faster, with an option to be backward compatible to the 'party' 
   implementation. The package is compatible with random forests fit using the 
   'party' and the 'randomForest' package. The methods are described in
   Strobl et al. (2007) <doi:10.1186/1471-2105-8-25> and 
   Debeer and Strobl (2020) <doi:10.1186/s12859-020-03622-2>.
	"""
	
	cran = "permimp" 

	version("1.0-2", md5="33385cb16482634dad7f248276efb06d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ipred@0.9.6:", type=("build", "run"))
	depends_on("r-party@1.3.3:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-survival@2.44.1.1:", type=("build", "run"))
