# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRexpokit(RPackage):
	"""R Wrappers for EXPOKIT; Other Matrix Functions

	Wraps some of the matrix exponentiation 
        utilities from EXPOKIT (<http://www.maths.uq.edu.au/expokit/>), 
        a FORTRAN library that is widely recommended for matrix 
        exponentiation (Sidje RB, 1998. "Expokit: A Software Package
        for Computing Matrix Exponentials." ACM Trans. Math. Softw.
        24(1): 130-156).  EXPOKIT includes functions for 
        exponentiating both small, dense matrices, and large, sparse
        matrices (in sparse matrices, most of the cells have value 0).
        Rapid matrix exponentiation is useful in phylogenetics when we 
        have a large number of states (as we do when we are inferring 
        the history of transitions between the possible geographic 
        ranges of a species), but is probably useful in other ways as 
        well. NOTE: In case FORTRAN checks temporarily get rexpokit 
        archived on CRAN, see archived binaries at GitHub in: 
        nmatzke/Matzke_R_binaries (binaries install without compilation 
        of source code).
	"""
	
	homepage = "http://phylo.wikidot.com/rexpokit"
	cran = "rexpokit" 

	version("0.26.6.14", md5="7e7d323bc5b31bb11e43e4be1a4ecd39")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
