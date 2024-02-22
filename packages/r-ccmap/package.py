# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmap(RPackage):
	"""Combination Connectivity Mapping

	Finds drugs and drug combinations that are predicted to reverse or mimic gene expression signatures. These drugs might reverse diseases or mimic healthy lifestyles.
	"""
	
	bioc = "ccmap" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ccmap_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ccmap/ccmap_1.28.0.tar.gz"]

	version("1.28.0", md5="d01f3e9dca6ce3403096f8fc00766755")

	depends_on("r-annotationdbi@1.36.2:", type=("build", "run"))
	depends_on("r-biocmanager@1.30.4:", type=("build", "run"))
	depends_on("r-ccdata@1.1.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-xgboost@0.6.4:", type=("build", "run"))
	depends_on("r-lsa@0.73.1:", type=("build", "run"))
