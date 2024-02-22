# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlft(RPackage):
	"""Processing Linear Features

	Assists in the manipulation and processing of linear features with the help of the 'sf' package.
  Makes use of linear referencing to extract data from most shape files.
  Reference for this packages methods: Albeke, S.E. et al. (2010) <doi:10.1007/s10980-010-9528-4>.
	"""
	
	cran = "rLFT" 

	version("1.0.1", md5="67cb593a70139a36ec6a7588896cd963")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf@0.9.1:", type=("build", "run"))
