# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbsurv(RPackage):
	"""Robust likelihood-based survival modeling with microarray data

	This package selects genes associated with survival.
	"""
	
	homepage = "http://www.korea.ac.kr/~stat2242/"
	bioc = "rbsurv" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rbsurv_2.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rbsurv/rbsurv_2.60.0.tar.gz"]

	version("2.60.0", md5="e2791c7a40004e031fd88e0995f4dc13")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
