# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvr(RPackage):
	"""Total Variation Regularization

	Provides tools for denoising noisy signal and images via
    Total Variation Regularization. Reducing the total variation of
    the given signal is known to remove spurious detail while preserving
    essential structural details. For the seminal work on the topic,
    see Rudin et al (1992) <doi:10.1016/0167-2789(92)90242-F>.
	"""
	
	homepage = "https://github.com/kisungyou/tvR"
	cran = "tvR" 

	version("0.3.2", md5="80cd8f1d9c8c320ee9ba8b2247ba49b9")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
