# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmsn(RPackage):
	"""Scale-Shape Mixtures of Skew-Normal Distributions

	It provides the density and random number generator for the Scale-Shape Mixtures of Skew-Normal Distributions proposed by Jamalizadeh and Lin (2016) <doi:10.1007/s00180-016-0691-1>.
	"""
	
	cran = "ssmsn" 

	version("0.2.0", md5="d3f71b6cffa348f7c3fa5170fc0cb1ac")

	depends_on("r-mcmcpack", type=("build", "run"))
