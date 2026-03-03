# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnlfa(RPackage):
	"""Moderated Nonlinear Factor Analysis

	
    Conducts moderated nonlinear factor analysis (e.g., Curran et al., 2014,
    <doi:10.1080/00273171.2014.889594>). 
    Regularization methods are implemented for assessing non-invariant items. 
    Currently, the package includes dichotomous items and unidimensional
    item response models. Extensions will be included in future package
    versions.
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/mnlfa"
	cran = "mnlfa" 

	version("0.3-4", md5="907631d431c41c8fff1bb41f8fcd02ce")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cdm@7.0.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
