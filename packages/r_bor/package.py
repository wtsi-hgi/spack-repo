# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBor(RPackage):
	"""Transforming Behavioral Observation Records into Data Matrices

	Transforms focal observations' data, where different types of social interactions
  can be recorded by multiple observers, into asymmetric data matrices.
  Each cell in these matrices provides counts on the number of times
  a specific type of social interaction was initiated by the row subject and
  directed to the column subject.
	"""
	
	cran = "bor" 

	version("0.1.0", md5="a154d33be0dac5debaf00903295164e8")

	depends_on("r@2.10:", type=("build", "run"))
