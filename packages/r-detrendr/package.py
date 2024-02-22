# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetrendr(RPackage):
	"""Detrend Images

	Detrend fluorescence microscopy image series for fluorescence
    fluctuation and correlation spectroscopy ('FCS' and 'FFS') analysis.
    This package contains functionality published in a 2016 paper
    <doi:10.1093/bioinformatics/btx434> but it has been extended since
    then with the Robin Hood algorithm and thus contains unpublished work.
	"""
	
	homepage = "https://rorynolan.github.io/detrendr/"
	cran = "detrendr" 

	version("0.6.15", md5="e53df63f4b346dfc38d816dfa94b068c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-arrayhelpers@1.1:", type=("build", "run"))
	depends_on("r-autothresholdr@1.3.11:", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-filesstrings@3.2.4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ijtiff@2.2:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.7:", type=("build", "run"))
	depends_on("r-rlang@0.3.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
