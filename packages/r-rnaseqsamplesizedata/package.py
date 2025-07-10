# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqsamplesizedata(RPackage):
	"""RnaSeqSampleSizeData

	RnaSeqSampleSizeData package provides the read counts and dispersion distribution from real RNA-seq experiments. It can be used by RnaSeqSampleSize package to estimate sample size and power for RNA-seq experiment design.
	"""
	
	bioc = "RnaSeqSampleSizeData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnaSeqSampleSizeData_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnaSeqSampleSizeData/RnaSeqSampleSizeData_1.34.0.tar.gz"]

	version("1.34.0", sha256="4e6668968830e4954653ca47c74c74925a5b9d38af0f023d495d0162e13d585c")

	depends_on("r-edger", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))

