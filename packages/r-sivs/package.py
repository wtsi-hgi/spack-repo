# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSivs(RPackage):
	"""Stable Iterative Variable Selection

	An iterative feature selection method (manuscript submitted) that
    internally utilizes various Machine Learning methods that have embedded
    feature reduction in order to shrink down the feature space into a small
    and yet robust set.
	"""
	
	homepage = "https://github.com/mmahmoudian/sivs"
	cran = "sivs" 

	version("0.2.10", md5="9e75131791822aefc21e4ae0eceb1b71")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
