# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDasst(RPackage):
	"""Tools for Reading, Processing and Writing 'DSSAT' Files

	Provides methods for reading, displaying,
    processing and writing files originally arranged for
    the 'DSSAT-CSM' fixed width format. The 'DSSAT-CSM' 
    cropping system model is described at J.W. Jones,
    G. Hoogenboomb, C.H. Porter, K.J. Boote, W.D. Batchelor,
    L.A. Hunt, P.W. Wilkens, U. Singh, A.J. Gijsman, 
    J.T. Ritchie (2003) <doi:10.1016/S1161-0301(02)00107-7>.
	"""
	
	cran = "Dasst" 

	version("0.3.4", md5="08d11ffa176048e8230ab5529536e144")

	depends_on("r@2.14:", type=("build", "run"))
