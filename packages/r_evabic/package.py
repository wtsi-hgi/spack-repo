# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvabic(RPackage):
	"""Evaluation of Binary Classifiers

	Evaluates the performance of binary classifiers.  Computes
    confusion measures (TP, TN, FP, FN), derived measures (TPR, FDR,
    accuracy, F1, DOR, ..), and area under the curve.  Outputs are well
    suited for nested dataframes.
	"""
	
	homepage = "https://abichat.github.io/evabic/"
	cran = "evabic" 

	version("0.1.1", md5="192a5dd609499246d3b9c303f2ab3a91")

