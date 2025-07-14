# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigcheck(RPackage):
	"""Check a gene signature's prognostic performance against random signatures, known signatures, and permuted data/metadata

	While gene signatures are frequently used to predict phenotypes (e.g. predict prognosis of cancer patients), it it not always clear how optimal or meaningful they are (cf David Venet, Jacques E. Dumont, and Vincent Detours' paper "Most Random Gene Expression Signatures Are Significantly Associated with Breast Cancer Outcome"). Based on suggestions in that paper, SigCheck accepts a data set (as an ExpressionSet) and a gene signature, and compares its performance on survival and/or classification tasks against a) random gene signatures of the same length; b) known, related and unrelated gene signatures; and c) permuted data and/or metadata.
	"""
	
	bioc = "SigCheck"

	version("2.40.0", commit="3fd401cc02e2c329ce31df894125305caf62a26b")
	version("2.34.0", commit="b39b362a1cae110f87390849f928938a252f1f6b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mlinterfaces", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
