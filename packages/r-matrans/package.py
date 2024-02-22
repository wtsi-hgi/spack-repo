# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrans(RPackage):
	"""Model Averaging-Assisted Optimal Transfer Learning

	Transfer learning, as a prevailing technique in computer sciences, aims to improve the performance of a target model by leveraging auxiliary information from heterogeneous source data. We provide novel tools for multi-source transfer learning under statistical models based on model averaging strategies, including linear regression models, partially linear models. Unlike existing transfer learning approaches, this method integrates the auxiliary information through data-driven weight assignments to avoid negative transfer. This is the first package for transfer learning based on the optimal model averaging frameworks, providing efficient implementations for practitioners in multi-source data modeling. The details are described in Hu and Zhang (2023) <https://jmlr.org/papers/v24/23-0030.html>.
	"""
	
	cran = "matrans" 

	version("0.1.0", md5="fbe88c53be9dea2b68d2954e2200fb96")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
