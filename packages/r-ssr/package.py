# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsr(RPackage):
	"""Semi-Supervised Regression Methods

	An implementation of semi-supervised regression methods including self-learning and co-training by committee based on Hady, M. F. A., Schwenker, F., & Palm, G. (2009) <doi:10.1007/978-3-642-04274-4_13>. Users can define which set of regressors to use as base models from the 'caret' package, other packages, or custom functions.
	"""
	
	homepage = "https://github.com/enriquegit/ssr"
	cran = "ssr" 

	version("0.1.1", md5="170cf42f7668aae016a6c582fac18235")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
