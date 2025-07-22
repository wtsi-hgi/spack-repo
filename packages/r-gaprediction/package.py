# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaprediction(RPackage):
	"""Prediction of gestational age with Illumina HumanMethylation450 data

	[GAprediction] predicts gestational age using Illumina HumanMethylation450 CpG data.
	"""
	
	bioc = "GAprediction" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GAprediction_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GAprediction/GAprediction_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="9fcb8d230ce07dcb0da19076f69db1929b3fe9e0f259145b3fdf40b2ec3ac6da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
