# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeebamviews(RPackage):
	"""leeBamViews -- multiple yeast RNAseq samples excerpted from Lee 2009

	data from PMID 19096707; prototype for managing multiple NGS samples
	"""
	
	bioc = "leeBamViews" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/leeBamViews_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/leeBamViews/leeBamViews_1.38.0.tar.gz"]

	version("1.38.0", md5="58f7c7fdbb1f949f48924ac79d31b580")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rsamtools@0.1.50:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))

	# experiment