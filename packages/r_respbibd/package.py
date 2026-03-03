# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRespbibd(RPackage):
	""""Resolvable Partially Balanced Incomplete Block Designs
(PBIBDs)"

	A collection of several utility functions related to resolvable and affine resolvable Partially Balanced Incomplete Block Designs (PBIBDs), have been developed. In the class of resolvable designs, affine resolvable designs are said to be optimal, Bailey (1995) <doi:10.2307/2337638>. Here, the package contains three functions to generate and study the characterization properties of these designs. Developed functions are named as PBIBD1(), PBIBD2() and PBIBD3(), in which first two functions are used to generate two new series of affine resolvable PBIBDs and last one is used to generate a new series of resolvable PBIBDs, respectively.  In addition, these functions can also be used to generate design parameters (v, b, r and k), canonical efficiency factors, variance factor between associates and average variance factors of the generated designs. Here v is the number of treatments, b (= b1 + b2, in case of non-proper design) is the number of blocks, r is the number of replications and k (= k1 + k2; k1 is the size of b1 and k2 is the size of b2) is the block size. 
	"""
	
	cran = "ResPBIBD" 

	version("0.1.0", md5="1e48c6d5ec38a7f3525d5cc8a435717f")

