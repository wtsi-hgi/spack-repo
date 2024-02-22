# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepsd(RPackage):
	"""Root Expected Proportion Squared Difference for Detecting DIF

	Root Expected Proportion Squared Difference (REPSD) is a nonparametric
  differential item functioning (DIF) method that (a) allows practitioners 
  to explore for DIF related to small, fine-grained focal groups of examinees, 
  and (b) compares the focal group directly to the composite group that will be 
  used to develop the reported test score scale. Using your provided response 
  matrix with a column that identifies focal group membership, this package
  provides the REPSD values, a simulated null distribution of possible REPSD
  values, and the simulated p-values identifying items possibly displaying DIF 
  without requiring enormous sample sizes.
	"""
	
	cran = "repsd" 

	version("1.0.1", md5="8be9083c3e2f0f2ed214fa7b27a83f04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
