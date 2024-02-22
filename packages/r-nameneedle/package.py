# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNameneedle(RPackage):
	"""Using Needleman-Wunsch to Match Sample Names

	The Needleman-Wunsch global alignment algorithm can be
  used to find approximate matches between sample names in different
  data sets. See Wang et al. (2010) <doi:10.4137/CIN.S5613>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "NameNeedle" 

	version("1.2.7", md5="45d9b4c3410e24b4a1e6dc3a602e9037")

	depends_on("r@3:", type=("build", "run"))
