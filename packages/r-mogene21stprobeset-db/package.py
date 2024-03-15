# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene21stprobesetDb(RPackage):
	"""Affymetrix mogene21 annotation data (chip mogene21stprobeset)

	Affymetrix mogene21 annotation data (chip mogene21stprobeset) assembled using data from public repositories
	"""
	
	bioc = "mogene21stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene21stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene21stprobeset.db/mogene21stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="d6b3c352329b46493a20f6c27db05d43")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation