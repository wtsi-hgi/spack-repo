# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsurf(RPackage):
	"""Variable Selection Using Random Forests

	Three steps variable selection procedure based on random forests.
    Initially developed to handle high dimensional data (for which number of
    variables largely exceeds number of observations), the package is very
    versatile and can treat most dimensions of data, for regression and
    supervised classification problems. First step is dedicated to eliminate
    irrelevant variables from the dataset. Second step aims to select all
    variables related to the response for interpretation purpose. Third step
    refines the selection by eliminating redundancy in the set of variables
    selected by the second step, for prediction purpose.
    Genuer, R. Poggi, J.-M. and Tuleau-Malot, C. (2015)
    <https://journal.r-project.org/archive/2015-2/genuer-poggi-tuleaumalot.pdf>.
	"""
	
	homepage = "https://github.com/robingenuer/VSURF"
	cran = "VSURF" 

	version("1.2.0", md5="ab83812bfc94ba78c91469e8aa182eb8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
