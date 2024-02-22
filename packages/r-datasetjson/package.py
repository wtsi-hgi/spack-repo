# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasetjson(RPackage):
	"""Read and Write CDISC Dataset JSON Files

	Read, construct and write CDISC (Clinical Data Interchange Standards Consortium) Dataset JSON (JavaScript Object Notation) files, while validating per the Dataset JSON schema file, as described in CDISC (2023) <https://www.cdisc.org/dataset-json>.
	"""
	
	homepage = "https://github.com/atorus-research/datasetjson"
	cran = "datasetjson" 

	version("0.2.0", md5="5cdd7c91f47727d926f6a5936d0b074c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-jsonvalidate@1.3.1:", type=("build", "run"))
