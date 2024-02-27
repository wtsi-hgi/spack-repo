# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHg1860merExpr(RPackage):
	"""Platform Design Info for NimbleGen hg18_60mer_expr

	Platform Design Info for NimbleGen hg18_60mer_expr
	"""
	
	bioc = "pd.hg18.60mer.expr" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.hg18.60mer.expr_3.12.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pd.hg18.60mer.expr/pd.hg18.60mer.expr_3.12.0.tar.gz"]

	version("3.12.0", md5="ee8d3813f74edce4e796933aa63999fb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

	# annotation