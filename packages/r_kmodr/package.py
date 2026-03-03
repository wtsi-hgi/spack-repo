# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmodr(RPackage):
	"""K-Means with Simultaneous Outlier Detection

	An implementation of the 'k-means--' algorithm proposed
    by Chawla and Gionis, 2013 in their paper,
    "k-means-- : A unified approach to clustering and outlier detection.
    SIAM International Conference on Data Mining (SDM13)",
    <doi:10.1137/1.9781611972832.21>
    and using 'ordering' described by Howe, 2013 in the thesis,
    Clustering and anomaly detection in tropical cyclones".
    Useful for creating (potentially) tighter clusters than
    standard k-means and simultaneously finding outliers inexpensively
    in multidimensional space.
	"""
	
	cran = "kmodR" 

	version("0.2.0", md5="e1508065fc6b7d45cf31120d2617f20f")

