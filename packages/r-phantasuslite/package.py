# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhantasuslite(RPackage):
	"""Loading and annotation RNA-Seq counts matrices

	PhantasusLite – a lightweight package with helper functions of general interest extracted from phantasus package. In parituclar it simplifies working with public RNA-seq datasets from GEO by providing access to the remote HSDS repository with the precomputed gene counts from ARCHS4 and DEE2 projects.
	"""
	
	homepage = "https://github.com/ctlab/phantasusLite/"
	bioc = "phantasusLite" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/phantasusLite_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/phantasusLite/phantasusLite_1.0.0.tar.gz"]

	version("1.0.0", sha256="8a2f8cd5194d5e3c3626d2e80fb27a0f98cada91ec8c59d2466b744b0105055f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rhdf5client@1.21.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
