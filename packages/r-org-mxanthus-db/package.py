# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgMxanthusDb(RPackage):
	"""Genome wide annotation for Myxococcus xanthus DK 1622

	Genome wide annotation for Myxococcus xanthus DK 1622, primarily based on mapping using Gene identifiers.
	"""
	
	bioc = "org.Mxanthus.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/org.Mxanthus.db_1.0.27.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/org.Mxanthus.db/org.Mxanthus.db_1.0.27.tar.gz"]

	version("1.0.27", md5="e493814c41401de383b4f6e0f3d39619")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationhub@1.46:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-biocfilecache@1.10.1:", type=("build", "run"))

	# annotation