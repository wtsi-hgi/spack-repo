# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotationforest(RPackage):
	"""Fit and Deploy Rotation Forest Models

	Fit and deploy rotation forest models ("Rodriguez, J.J., Kuncheva,
    L.I., 2006. Rotation forest: A new classifier ensemble method. IEEE Trans.
    Pattern Anal. Mach. Intell. 28, 1619-1630 <doi:10.1109/TPAMI.2006.211>") for binary classification.
    Rotation forest is an ensemble method where each base classifier (tree) is
    fit on the principal components of the variables of random partitions of
    the feature set.
	"""
	
	cran = "rotationForest" 

	version("0.1.3", md5="ed16c6b99ea23e905150503661f98b62")

	depends_on("r-rpart", type=("build", "run"))
