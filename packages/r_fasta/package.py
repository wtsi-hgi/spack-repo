# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasta(RPackage):
	"""Fast Adaptive Shrinkage/Thresholding Algorithm

	A collection of acceleration schemes for proximal gradient methods for estimating penalized regression parameters described in
    Goldstein, Studer, and Baraniuk (2016) <arXiv:1411.3406>. Schemes such as Fast Iterative Shrinkage and Thresholding Algorithm (FISTA) by Beck and Teboulle (2009) <doi:10.1137/080716542> 
    and the adaptive stepsize rule introduced in Wright, Nowak, and Figueiredo (2009) <doi:10.1109/TSP.2009.2016892> are included. You provide the objective function and proximal mappings, and it takes care of the issues like stepsize selection, acceleration, and stopping conditions for you.
	"""
	
	cran = "fasta" 

	version("0.1.0", md5="c522baefc19fd7a1bc1976da2f93fc1d")

