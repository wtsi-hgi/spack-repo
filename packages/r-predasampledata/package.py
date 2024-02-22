# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredasampledata(RPackage):
	"""expression and copy number data on clear cell renal carcinoma samples

	Sample data for PREDA package. (annotations objects synchronized with GeneAnnot custom CDFs version 2.2.0)
	"""
	
	bioc = "PREDAsampledata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/PREDAsampledata_0.42.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/PREDAsampledata/PREDAsampledata_0.42.0.tar.gz"]

	version("0.42.0", md5="5acce57384c00a56d658281ba4fa57e5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-preda", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))

	# experiment