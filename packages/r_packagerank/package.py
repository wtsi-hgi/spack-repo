# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackagerank(RPackage):
	"""Computation and Visualization of Package Download Counts and
Percentiles

	Compute and visualize the cross-sectional and longitudinal number
    and rank percentile of package downloads from Posit/RStudio's CRAN mirror.
	"""
	
	homepage = "https://github.com/lindbrook/packageRank"
	cran = "packageRank" 

	version("0.8.3", md5="4ce6bdc31e879aaa44d30de1a925bff4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pkgsearch", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rversions", type=("build", "run"))
	depends_on("r-sugrrants", type=("build", "run"))
