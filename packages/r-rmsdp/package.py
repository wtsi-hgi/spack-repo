# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmsdp(RPackage):
	"""Refined Modified Stahel-Donoho (MSD) Estimators for Outlier
Detection (Parallel Version)

	
    A parallel function for multivariate outlier detection named modified Stahel-Donoho estimators is contained in this package.  The function RMSDp() is for elliptically distributed datasets and recognizes outliers based on Mahalanobis distance. This function is for higher dimensional datasets that cannot be handled by a single core function RMSD() included in 'RMSD' package.  See Wada and Tsubaki (2013) <doi:10.1109/CLOUDCOM-ASIA.2013.86> for the detail of the algorithm. 
	"""
	
	cran = "RMSDp" 

	version("0.1.0", md5="1ba73263582839070370f382bd60f33d")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
