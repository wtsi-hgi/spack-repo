# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAll(RPackage):
	"""A data package

	Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz Laboratory at the DFCI (includes Apr 2004 versions)
	"""
	
	bioc = "ALL" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ALL_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ALL/ALL_1.44.0.tar.gz"]

	version("1.44.0", md5="b80eb482b4937ef4eac01027ac95a61a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment