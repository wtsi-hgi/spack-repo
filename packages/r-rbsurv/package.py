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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rbsurv_2.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rbsurv/rbsurv_2.60.0.tar.gz"]

    version("2.66.0", tag="RELEASE_3_21")
	version("2.60.0", sha256="90a9b4d776c70ec276addfd9bd6af67d9ab4080dd7262974142a23f961ab7a06")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
