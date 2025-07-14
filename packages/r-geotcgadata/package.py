# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeotcgadata(RPackage):
	"""Processing Various Types of Data on GEO and TCGA

	Gene Expression Omnibus(GEO) and The Cancer Genome Atlas (TCGA) provide us with a wealth of data, such as RNA-seq, DNA Methylation, SNP and Copy number variation data. It's easy to download data from TCGA using the gdc tool, but processing these data into a format suitable for bioinformatics analysis requires more work. This R package was developed to handle these data.
	"""
	
	homepage = "https://github.com/YuLab-SMU/GeoTcgaData"
	bioc = "GeoTcgaData"

	version("2.8.0", commit="a6a54a46977a9980ff24a302f0fbf68901497398")
	version("2.2.0", commit="e239614918c87af90a0cf7c7f2de0c3607cc7c9a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cqn", type=("build", "run"))
	depends_on("r-topconfects", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
