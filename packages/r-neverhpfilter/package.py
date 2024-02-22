# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeverhpfilter(RPackage):
	"""An Alternative to the Hodrick-Prescott Filter

	In the working paper titled "Why You Should Never Use the Hodrick-Prescott 
   Filter", James D. Hamilton proposes a new alternative to economic time series 
   filtering. The neverhpfilter package provides functions and data for reproducing his work. Hamilton (2017) <doi:10.3386/w23429>.
	"""
	
	homepage = "https://justinmshea.github.io/neverhpfilter/"
	cran = "neverhpfilter" 

	version("0.4-0", md5="5c80698c6a2975794cdfb7db98b47c53")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts@0.11.0:", type=("build", "run"))
	depends_on("r-zoo@1.8.0:", type=("build", "run"))
