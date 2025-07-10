# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoberts2005annotationDb(RPackage):
	"""Roberts2005Annotation Annotation Data (Roberts2005Annotation)

	Roberts2005Annotation Annotation Data (Roberts2005Annotation) assembled using data from public repositories
	"""
	
	bioc = "Roberts2005Annotation.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Roberts2005Annotation.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Roberts2005Annotation.db/Roberts2005Annotation.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="ea195971251cf045fd6f0bfc6784aacf76e73c04c82856f2fac79ad10d2b89b9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

