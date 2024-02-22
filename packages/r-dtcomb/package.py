# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtcomb(RPackage):
	"""Statistical Combination of Diagnostic Tests

	A system for combining two diagnostic tests using various approaches
              that include statistical and machine-learning-based methodologies. 
              These approaches are divided into four groups: linear combination 
              methods, non-linear combination methods, mathematical operators, 
              and machine learning algorithms. See 
              the <https://biotools.erciyes.edu.tr/dtComb/> website 
              for more information, documentation, and examples.
	"""
	
	homepage = "https://github.com/gokmenzararsiz/dtComb"
	cran = "dtComb" 

	version("1.0.2", md5="039224e7301d176d152b606cd9d87675")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-proc@1.18:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-optimalcutpoints", type=("build", "run"))
