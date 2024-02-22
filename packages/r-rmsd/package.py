# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmsd(RPackage):
	"""Refined Modified Stahel-Donoho Estimators for Outlier Detection

	
     A function for multivariate outlier detection named Modified Stahel-Donoho (MSD) estimators is contained.  The function is for elliptically distributed datasets and recognizes outliers based on Mahalanobis distance. 
    The function is called the single core version in Wada & Tsubaki (2013) <doi:10.1109/CLOUDCOM-ASIA.2013.86> and evaluated with other methods in Wada, Kawano & Tsubaki (2020) <doi:10.17713/ajs.v49i2.872>.
	"""
	
	cran = "RMSD" 

	version("0.1.0", md5="d046c38458616cfe17e3b742f971b388")

