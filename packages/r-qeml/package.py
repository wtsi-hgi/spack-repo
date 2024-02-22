# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQeml(RPackage):
	"""Quick and Easy Machine Learning Tools

	The letters 'qe' in the package title stand for "quick and
   easy," alluding to the convenience goal of the package. We bring
   together a variety of machine learning (ML) tools from standard R
   packages, providing wrappers with a simple, convenient, 
   and uniform interface.
	"""
	
	homepage = "https://github.com/matloff/qeML"
	cran = "qeML" 

	version("1.1", md5="b597defc5fa93e27b824a75074af49f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-regtools@0.8:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tufte", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-toweranna", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-partools", type=("build", "run"))
	depends_on("r-foci", type=("build", "run"))
