# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrantham(RPackage):
	"""Calculate the 'Grantham' Distance

	A minimal set of routines to calculate the 'Grantham' distance
    <doi:10.1126/science.185.4154.862>. The 'Grantham' distance attempts to
    provide a proxy for the evolutionary distance between two amino acids
    based on three key chemical properties: composition, polarity and
    molecular volume. In turn, evolutionary distance is used as a proxy for
    the impact of missense mutations. The higher the distance, the more
    deleterious the substitution is expected to be.
	"""
	
	homepage = "https://maialab.org/grantham/"
	cran = "grantham" 

	version("0.1.1", md5="daf4e573ef2e79f28e914db57028a6ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
