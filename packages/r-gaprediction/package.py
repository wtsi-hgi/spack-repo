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

	version("1.34.0", commit="a055f672c2e9ff7adedb4ce2d5fef1145028771b")
	version("1.28.0", commit="d93600c3afe453298af124c0548365e9b8221264")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
