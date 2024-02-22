# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKamila(RPackage):
	"""Methods for Clustering Mixed-Type Data

	Implements methods for clustering mixed-type data,
  specifically combinations of continuous and nominal data. Special attention
  is paid to the often-overlooked problem of equitably balancing the
  contribution of the continuous and categorical variables. This package
  implements KAMILA clustering, a novel method for clustering
  mixed-type data in the spirit of k-means clustering. It does not require
  dummy coding of variables, and is efficient enough to scale to rather large
  data sets. Also implemented is Modha-Spangler clustering, which uses a
  brute-force strategy to maximize the cluster separation simultaneously in the
  continuous and categorical variables. For more information, see Foss, Markatou,
  Ray, & Heching (2016) <doi:10.1007/s10994-016-5575-7> and Foss & Markatou
  (2018) <doi:10.18637/jss.v083.i13>.
	"""
	
	homepage = "https://github.com/ahfoss/kamila"
	cran = "kamila" 

	version("0.1.2", md5="0888f5093910e8ff8daaca49a7bf388e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
