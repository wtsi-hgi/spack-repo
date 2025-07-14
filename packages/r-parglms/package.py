# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParglms(RPackage):
	"""support for parallelized estimation of GLMs/GEEs

	This package provides support for parallelized estimation of GLMs/GEEs, catering for dispersed data.
	"""
	
	bioc = "parglms"

	version("1.40.0", commit="acade9e8d3324273ca462d9705f2b4ba1c0be283")
	version("1.34.0", commit="610d733e186fe6fe782dc9011b98f3247634716f")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-batchjobs", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
