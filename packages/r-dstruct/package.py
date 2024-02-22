# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstruct(RPackage):
	"""Identifying differentially reactive regions from RNA structurome profiling data

	dStruct identifies differentially reactive regions from RNA structurome profiling data. dStruct is compatible with a broad range of structurome profiling technologies, e.g., SHAPE-MaP, DMS-MaPseq, Structure-Seq, SHAPE-Seq, etc. See Choudhary et al., Genome Biology, 2019 for the underlying method.
	"""
	
	homepage = "https://github.com/dataMaster-Kris/dStruct"
	bioc = "dStruct" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dStruct_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dStruct/dStruct_1.8.0.tar.gz"]

	version("1.8.0", md5="294cd694534f0d82a92aaabeea86836f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
