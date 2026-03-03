# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScutr(RPackage):
	"""Balancing Multiclass Datasets for Classification Tasks

	Imbalanced training datasets impede many popular classifiers. To balance training data, a combination of oversampling minority classes and undersampling majority classes is useful. This package implements the SCUT (SMOTE and Cluster-based Undersampling Technique) algorithm as described in Agrawal et. al. (2015) <doi:10.5220/0005595502260234>. Their paper uses model-based clustering and synthetic oversampling to balance multiclass training datasets, although other resampling methods are provided in this package.
	"""
	
	homepage = "https://github.com/s-kganz/scutr"
	cran = "scutr" 

	version("0.2.0", md5="36e6730f5ad37a1af6353bb5c640ed62")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
