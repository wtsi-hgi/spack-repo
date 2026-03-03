# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROxybs(RPackage):
	"""Processing of Oxy-Bisulfite Microarray Data

	
  Provides utilities for processing of Oxy-Bisulfite microarray data 
  (e.g. via the Illumina Infinium platform, <http://www.illumina.com>) 
  with tandem arrays, one using conventional
  bisulfite conversion, the other using oxy-bisulfite conversion.
	"""
	
	cran = "OxyBS" 

	version("1.5", md5="1643e7e493a34ed6ac0cdbb7a595fd4f")

	depends_on("r@3.2.2:", type=("build", "run"))
