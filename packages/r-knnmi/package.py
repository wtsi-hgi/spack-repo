# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnmi(RPackage):
	"""k-Nearest Neighbor Mutual Information Estimator

	This is a 'C++' mutual information (MI) library based on the k-nearest 
    neighbor (KNN) algorithm. There are three functions provided for computing MI 
    for continuous values, mixed continuous and discrete values, and conditional MI 
    for continuous values. They are based on algorithms by A. Kraskov, et. al. (2004) <doi:10.1103/PhysRevE.69.066138>, 
    BC Ross (2014)<doi:10.1371/journal.pone.0087357>, 
    and A. Tsimpiris (2012) <doi:10.1016/j.eswa.2012.05.014>, respectively.
	"""
	
	cran = "knnmi" 

	version("1.0", md5="f33a1eb2e0bbddefac3a72ce27d96b1d")

	depends_on("r@4.1:", type=("build", "run"))
