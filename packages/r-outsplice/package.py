# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutsplice(RPackage):
	"""Comparison of Splicing Events between Tumor and Normal Samples

	An easy to use tool that can compare splicing events in tumor and normal tissue samples using either a user generated matrix, or data from The Cancer Genome Atlas (TCGA). This package generates a matrix of splicing outliers that are significantly over or underexpressed in tumors samples compared to normal denoted by chromosome location. The package also will calculate the splicing burden in each tumor and characterize the types of splicing events that occur.
	"""
	
	homepage = "https://github.com/GuoLabUCSD/OutSplice"
	bioc = "OutSplice"

	version("1.8.0", commit="dfced8d8f8bb9a5db601fef3731d513372acb65a")
	version("1.2.0", commit="2035f79de46a9c4ced871bd2dcff16522eed1091")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-annotationdbi@1.60:", type=("build", "run"))
	depends_on("r-genomicranges@1.49:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.50.2:", type=("build", "run"))
	depends_on("r-iranges@2.32:", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.16:", type=("build", "run"))
	depends_on("r-repitools@1.44:", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene@3.2.2:", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene@3.16:", type=("build", "run"))
	depends_on("r-s4vectors@0.36:", type=("build", "run"))
