# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtpca(RPackage):
	"""Thermal proximity co-aggregation with R

	R package for performing thermal proximity co-aggregation analysis with thermal proteome profiling datasets to analyse protein complex assembly and (differential) protein-protein interactions across conditions.
	"""
	
	bioc = "Rtpca" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rtpca_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rtpca/Rtpca_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="ec0e64e6a26f7d0ff9c5ab734e1fd76f3272b2b57de5e2fa1a5309cd8f20ba93")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
