# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrroc(RPackage):
	"""Precision-Recall and ROC Curves for Weighted and Unweighted Data

	Computes the areas under the precision-recall (PR) and ROC curve for weighted (e.g., soft-labeled) and unweighted data. In contrast to other implementations, the interpolation between points of the PR curve is done by a non-linear piecewise function. In addition to the areas under the curves, the curves themselves can also be computed and plotted by a specific S3-method. References: Davis and Goadrich (2006) <doi:10.1145/1143844.1143874>; Keilwagen et al. (2014) <doi:10.1371/journal.pone.0092209>; Grau et al. (2015) <doi:10.1093/bioinformatics/btv153>.
	"""
	
	cran = "PRROC" 

	version("1.3.1", md5="a69d2bae6c1c3295b4d87a121b6a9ff4")

