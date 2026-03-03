# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraposas(RPackage):
	"""Graphical Approach Optimal Sample Size

	Graphical approach provides a useful framework for multiplicity adjustment in clinical trials with multiple endpoints. This package includes statistical methods to optimize sample size over initial weight and transition probability in a graphical approach under a common setting, which is to use marginal power for each endpoint in a trial design.
    See Zhang, F. and Gou, J. (2023). Sample size optimization for clinical trials using graphical approaches for multiplicity adjustment, Technical Report.
	"""
	
	cran = "graposas" 

	version("1.0.0", md5="b2b6f1ea01c3694c0cf5afaa67c6cf07")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ga@3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
