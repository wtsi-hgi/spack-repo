# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REclrmc(RPackage):
	"""Ensemble Correlation-Based Low-Rank Matrix Completion

	Ensemble correlation-based low-rank matrix completion method (ECLRMC) is an extension to the LRMC based methods. Traditionally, the LRMC based methods give identical importance to the whole data which results in emphasizing on the commonality of the data and overlooking the subtle but crucial differences. This method aims to overcome the equality assumption problem that exists in the current LRMS based methods. Ensemble correlation-based low-rank matrix completion (ECLRMC) takes consideration of the specific characteristic of each sample and performs LRMC on the set of samples with a strong correlation. It uses an ensemble learning method to improve the imputation performance. Since each sample is analyzed independently this method can be parallelized by distributing imputation across many computation units or GPU platforms. This package provides three different methods (LRMC, CLRMC and ECLRMC) for data imputation. There is also an NRMS function for evaluating the result. Chen, Xiaobo, et al (2017) <doi:10.1016/j.knosys.2017.06.010>.
	"""
	
	cran = "ECLRMC" 

	version("1.0", md5="e178ce4ebe0a06b692225138e54feeb1")

	depends_on("r-softimpute", type=("build", "run"))
