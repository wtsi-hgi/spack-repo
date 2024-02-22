# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpumatrix(RPackage):
	"""Basic Linear Algebra with GPU

	GPUs are great resources for data analysis, especially in statistics and linear algebra. Unfortunately, very few packages connect R to the GPU, and none of them are transparent enough to run the computations on the GPU without substantial changes to the code. The maintenance of these packages is cumbersome: several of the earlier attempts have been removed from their respective repositories. It would be desirable to have a properly maintained R package that takes advantage of the GPU with minimal changes to the existing code. We have developed the GPUmatrix package (available on CRAN). GPUmatrix mimics the behavior of the Matrix package and extends R to use the GPU for computations. It includes single(FP32) and double(FP64) precision data types, and provides support for sparse matrices. It is easy to learn, and requires very few code changes to perform the operations on the GPU. GPUmatrix relies on either the Torch or Tensorflow R packages to perform the GPU operations. We have demonstrated its usefulness for several statistical applications and machine learning applications: non-negative matrix factorization, logistic regression and general linear models. We have also included a comparison of GPU and CPU performance on different matrix operations.
	"""
	
	cran = "GPUmatrix" 

	version("1.0.1", md5="8ced8f02fc2afb65b8b16d381702a62f")

	depends_on("r@4.1:", type=("build", "run"))
