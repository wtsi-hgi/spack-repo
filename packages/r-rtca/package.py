# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtca(RPackage):
	"""Open-source toolkit to analyse data from xCELLigence System (RTCA)

	Import, analyze and visualize data from Roche(R) xCELLigence RTCA systems. The package imports real-time cell electrical impedance data into R. As an alternative to commercial software shipped along the system, the Bioconductor package RTCA provides several unique transformation (normalization) strategies and various visualization tools.
	"""
	
	homepage = "http://code.google.com/p/xcelligence/"
	bioc = "RTCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RTCA_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RTCA/RTCA_1.54.0.tar.gz"]

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="7f8c010d92dc423dd6d0d40385e4bffd57e5256dfbe11ffa5e2fd763e9466fc5")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
