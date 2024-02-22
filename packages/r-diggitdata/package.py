# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiggitdata(RPackage):
	"""Example data for the diggit package

	This package provides expression profile and CNV data for glioblastoma from TCGA, and transcriptional and post-translational regulatory networks assembled with the ARACNe and MINDy algorithms, respectively.
	"""
	
	bioc = "diggitdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/diggitdata_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/diggitdata/diggitdata_1.34.0.tar.gz"]

	version("1.34.0", md5="48dc6a1a35dae2169279a2766e3b56de")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))

	# experiment