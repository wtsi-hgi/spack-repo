# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArc(RPackage):
	"""Association Rule Classification

	Implements the Classification-based on
    Association Rules (CBA) algorithm for association rule classification.
    The package, also described in Hahsler et al. (2019) <doi:10.32614/RJ-2019-048>,
    contains several convenience methods that allow to automatically
    set CBA parameters (minimum confidence, minimum support) and it also natively
    handles numeric attributes by integrating a pre-discretization step.
    The rule generation phase is handled by the 'arules' package. 
    To further decrease the size of the CBA models produced by the 'arc' package, postprocessing by the 
    'qCBA' package is suggested.
	"""
	
	homepage = "https://github.com/kliegr/arc"
	cran = "arc" 

	version("1.4", md5="7e0cfa4f1f55e64307178935873e09af")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-arules@1.7.4:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-discretization", type=("build", "run"))
	depends_on("r-matrix@0.5.0:", type=("build", "run"))
