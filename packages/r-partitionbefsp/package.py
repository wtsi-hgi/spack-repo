# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartitionbefsp(RPackage):
	"""Methods for Calculating the Loreau & Hector 2001 BEF Partition

	A collection of functions that can be used to estimate selection and complementarity effects,
	sensu Loreau & Hector (2001) <doi:10.1038/35083573>, even in cases where data are only available for
	a random subset of species (i.e. incomplete sample-level data). A full derivation and explanation of the 
	statistical corrections used here is available in Clark et al. (2019) <doi:10.1111/2041-210X.13285>.
	"""
	
	cran = "partitionBEFsp" 

	version("1.0", md5="70a1922ec2d08c3e0a644d005196bc61")

	depends_on("r@3.4:", type=("build", "run"))
