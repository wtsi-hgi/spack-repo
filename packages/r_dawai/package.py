# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDawai(RPackage):
	"""Discriminant Analysis with Additional Information

	In applications it is usual that some additional          
      information is available. This package dawai (an acronym 
      for Discriminant Analysis With Additional Information) 
      performs linear and quadratic discriminant analysis with 
      additional information expressed as inequality restrictions 
      among the populations means. It also computes several 
      estimations of the true error rate.
	"""
	
	cran = "dawai" 

	version("1.2.6", md5="54e5531b7c0478f82045b5328330a827")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
