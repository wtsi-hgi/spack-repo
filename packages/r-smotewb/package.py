# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmotewb(RPackage):
	"""Imbalanced Resampling using SMOTE with Boosting (SMOTEWB)

	Provides the SMOTE with Boosting (SMOTEWB) algorithm. See
      F. Sağlam, M. A. Cengiz (2022) <doi:10.1016/j.eswa.2022.117023>. Also 
      SMOTEWB provides faster versions of several resampling methods for 
      imbalanced datasets, including SMOTE with Boosting (SMOTEWB), Random Walk 
      Oversampling (RWO), ADASYN, Borderline SMOTE (BLSMOTE), Random 
      Over-Sampling (ROS), Random Under-Sampling (RUS), Safe-Level SMOTE 
      (SLSMOTE), Relocating Safe-Level SMOTE (RSLSMOTE), and Random 
      Over-Sampling Examples (ROSE).
	"""
	
	cran = "SMOTEWB" 

	version("1.1.3", md5="0e9d3c8be7cf760bedd608d2b8fe0e1b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
