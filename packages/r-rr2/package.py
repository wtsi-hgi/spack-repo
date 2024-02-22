# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRr2(RPackage):
	"""R2s for Regression Models

	Three methods to calculate R2 for models with correlated errors, 
    including Phylogenetic GLS, Phylogenetic Logistic Regression, Linear Mixed 
    Models (LMMs), and Generalized Linear Mixed Models (GLMMs). See details in 
    Ives 2018 <doi:10.1093/sysbio/syy060>.
	"""
	
	homepage = "https://github.com/arives/rr2"
	cran = "rr2" 

	version("1.1.1", md5="28dba33ab3af55b181d149859930a381", url="https://cran.r-project.org/src/contrib/rr2_1.1.1.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-phylolm@2.6.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-phyr@1.0.3:", type=("build", "run"))
