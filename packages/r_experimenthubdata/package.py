# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimenthubdata(RPackage):
	"""Add resources to ExperimentHub

	Functions to add metadata to ExperimentHub db and resource files to AWS S3 buckets.
	"""
	
	bioc = "ExperimentHubData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ExperimentHubData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ExperimentHubData/ExperimentHubData_1.28.0.tar.gz"]

	version("1.28.0", md5="9e36d1a7958213cce85feccfd46fd7d5")

	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-annotationhubdata@1.21.3:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
