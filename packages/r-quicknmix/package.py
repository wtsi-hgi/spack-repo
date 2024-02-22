# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuicknmix(RPackage):
	"""Asymptotic N-Mixture Model Fitting

	For fitting N-mixture models using either FFT or asymptotic approaches. FFT N-mixture models extend the work of Cowen et al. (2017) <doi:10.1111/biom.12701>. Asymptotic N-mixture models extend the work of Dail and Madsen (2011) <doi:10.1111/j.1541-0420.2010.01465.x>, to consider asymptotic solutions to the open population N-mixture models. The FFT models are derived and described in "Parker, M.R.P., Elliott, L., Cowen, L.L.E. (2022). Computational efficiency and precision for replicated-count and batch-marked hidden population models [Manuscript in preparation]. Department of Statistics and Actuarial Sciences, Simon Fraser University.". The asymptotic models are derived and described in: "Parker, M.R.P., Elliott, L., Cowen, L.L.E., Cao, J. (2022). Fast asymptotic solutions for N-mixtures on large populations [Manuscript in preparation]. Department of Statistics and Actuarial Sciences, Simon Fraser University.".
	"""
	
	cran = "quickNmix" 

	version("1.1.1", md5="d48705e19daa25fbb31c6613155e10d9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
