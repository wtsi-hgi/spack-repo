# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizrdata(RPackage):
	"""Data Management API for epiviz interactive visualization app

	Serve data from Bioconductor Objects through a WebSocket connection.
	"""
	
	homepage = "http://epiviz.github.io"
	bioc = "epivizrData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epivizrData_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epivizrData/epivizrData_1.30.0.tar.gz"]

	version("1.30.0", md5="aa9cf42fdbb0ad293964de33fc62e27a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-epivizrserver@1.1.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@0.2:", type=("build", "run"))
	depends_on("r-organismdbi", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
