# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResourceselection(RPackage):
	"""Resource Selection (Probability) Functions for Use-Availability
Data

	Resource Selection (Probability) Functions
  for use-availability wildlife data
  based on weighted distributions as described in
  Lele and Keim (2006) <doi:10.1890/0012-9658(2006)87%5B3021:WDAEOR%5D2.0.CO;2>,
  Lele (2009) <doi:10.2193/2007-535>,
  and Solymos & Lele (2016) <doi:10.1111/2041-210X.12432>.
	"""
	
	homepage = "https://github.com/psolymos/ResourceSelection"
	cran = "ResourceSelection" 

	version("0.3-6", md5="ce3bc8f0ef89cbab482f06345e206f86")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
