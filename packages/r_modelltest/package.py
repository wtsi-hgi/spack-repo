# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelltest(RPackage):
	"""Compare Models with Cross-Validated Log-Likelihood

	An implementation of the cross-validated difference in means (CVDM) test by Desmarais and Harden (2014) <doi:10.1007/s11135-013-9884-7> (see also Harden and Desmarais, 2011 <doi:10.1177/1532440011408929>) and the cross-validated median fit (CVMF) test by Desmarais and Harden (2012) <doi:10.1093/pan/mpr042>. These tests use leave-one-out cross-validated log-likelihoods to assist in selecting among model estimations. You can also utilize data from Golder (2010) <doi:10.1177/0010414009341714> and Joshi & Mason (2008) <doi:10.1177/0022343308096155> that are included to facilitate examples from real-world analysis.
	"""
	
	homepage = "https://github.com/ShanaScogin/modeLLtest"
	cran = "modeLLtest" 

	version("1.0.4", md5="1ce10a92b8c69c2414e1522103176467")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-coxrobust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
