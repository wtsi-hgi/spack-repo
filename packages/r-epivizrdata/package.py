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

	version("1.36.0", commit="2dadce9be3df397108d7471759436152b5b20aed")
	version("1.30.0", commit="83031e55f4eed0ed8452ee7801a809a6cb6a90e0")

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
