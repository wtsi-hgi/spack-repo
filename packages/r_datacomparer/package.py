# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatacomparer(RPackage):
	"""Compare Two Data Frames and Summarise the Difference

	Easy comparison of two tabular data
    objects in R. Specifically designed to show differences between two sets of
    data in a useful way that should make it easier to understand the differences,
    and if necessary, help you work out how to remedy them. Aims
    to offer a more useful output than all.equal() when your two data sets do not
    match, but isn't intended to replace all.equal() as a way to test for equality.
	"""
	
	homepage = "https://github.com/capitalone/dataCompareR"
	cran = "dataCompareR" 

	version("0.1.4", md5="3307a54bac5af91d8ca1eca0b4b56859")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
