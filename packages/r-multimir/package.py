# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimir(RPackage):
	"""Integration of multiple microRNA-target databases with their disease and drug associations

	A collection of microRNAs/targets from external resources, including validated microRNA-target databases (miRecords, miRTarBase and TarBase), predicted microRNA-target databases (DIANA-microT, ElMMo, MicroCosm, miRanda, miRDB, PicTar, PITA and TargetScan) and microRNA-disease/drug databases (miR2Disease, Pharmaco-miR VerSe and PhenomiR).
	"""
	
	homepage = "https://github.com/KechrisLab/multiMiR"
	bioc = "multiMiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multiMiR_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multiMiR/multiMiR_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="2574a7991c9552c84c8cd9c39ba4f5508d6e21870a0126da1ff855e96c82b157")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
