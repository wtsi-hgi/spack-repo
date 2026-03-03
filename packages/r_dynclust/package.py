# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynclust(RPackage):
	"""Denoising and Clustering for Dynamical Image Sequence (2D or
3D)+t

	A two-stage procedure for the denoising and clustering of stack of noisy images acquired over time. Clustering only assumes that the data contain an unknown but small number of dynamic features. The method first denoises the signals using local spatial and full temporal information. The clustering step uses the previous output to aggregate voxels based on the knowledge of their spatial neighborhood. Both steps use a single keytool based on the statistical comparison of the difference of two signals with the null signal. No assumption is therefore required on the shape of the signals. The data are assumed to be normally distributed (or at least follow a symmetric distribution) with a known constant variance. Working pixelwise, the method can be time-consuming depending on the size of the data-array but harnesses the power of multicore cpus.
	"""
	
	cran = "DynClust" 

	version("3.24", md5="c560c9b5d7ec5b3c889b6d04f7ae058a")

	depends_on("r@2.10:", type=("build", "run"))
