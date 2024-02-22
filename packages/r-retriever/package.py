# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetriever(RPackage):
	"""Generate Disease-Specific Response Signatures from the
LINCS-L1000 Data

	Generates disease-specific drug-response profiles that are independent of time, concentration, and cell-line. Based on the cell lines used as surrogates, the returned profiles represent the unique transcriptional changes induced by a compound in a given disease.
	"""
	
	cran = "retriever" 

	version("0.2.1", md5="d942013f44d235f11cdd45430cf37fe6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
