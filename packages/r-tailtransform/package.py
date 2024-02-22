# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTailtransform(RPackage):
	"""Symmetric Transformation of Tails for Plotting Differences

	When plotting treated-minus-control differences, after-minus-before changes, or difference-in-differences, the ttrans() function symmetrically transforms the positive and negative tails to aid plotting.  The package includes an observational study with three control groups and an unaffected outcome; see Rosenbaum (2020) <doi:10.1111/biom.13558>.
	"""
	
	cran = "tailTransform" 

	version("1.0.4", md5="78f4f332c6d6cc3682729c7754855249")

	depends_on("r@3.5:", type=("build", "run"))
