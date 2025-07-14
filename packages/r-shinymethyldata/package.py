# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymethyldata(RPackage):
	"""Example dataset of input data for shinyMethyl

	Extracted data from 369 TCGA Head and Neck Cancer DNA methylation samples. The extracted data serve as an example dataset for the package shinyMethyl. Original samples are from 450k methylation arrays, and were obtained from The Cancer Genome Atlas (TCGA). 310 samples are from tumor, 50 are matched normals and 9 are technical replicates of a control cell line.
	"""
	
	bioc = "shinyMethylData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/shinyMethylData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/shinyMethylData/shinyMethylData_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="306060c3ba13b0d69b912bfecf8e14db0f11f7d9874668cd9bf7c974e273cec4")

	depends_on("r@3:", type=("build", "run"))

