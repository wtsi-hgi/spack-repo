# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollutils(RPackage):
	"""Auxiliary Package for Package 'CollapsABEL'

	Provides some low level functions for processing PLINK input and output files.
	"""
	
	homepage = "https://bitbucket.org/kindlychung/collutils"
	cran = "collUtils" 

	version("1.0.5", md5="2f0966ba9357ee61de55a910de883954")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rjava@0.9.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
