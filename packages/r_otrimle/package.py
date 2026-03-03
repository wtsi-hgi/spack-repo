# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtrimle(RPackage):
	"""Robust Model-Based Clustering

	Performs robust cluster analysis allowing for outliers and noise that cannot be fitted by any cluster. The data are modelled by a mixture of Gaussian distributions and a noise component, which is an improper uniform  distribution covering the whole Euclidean space. Parameters are estimated by  (pseudo) maximum likelihood. This is fitted by a EM-type algorithm. See Coretto and Hennig (2016) <doi:10.1080/01621459.2015.1100996>, and Coretto and Hennig (2017) <https://jmlr.org/papers/v18/16-382.html>.
	"""
	
	cran = "otrimle" 

	version("2.0", md5="b951e8ea7e9e71afd4ff99f10ffa46f7")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
