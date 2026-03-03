# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootgof(RPackage):
	"""Bootstrap Based Goodness-of-Fit Tests

	Bootstrap based goodness-of-fit tests. It allows
    to perform rigorous statistical tests to check if a chosen
    model family is correct based on the marked empirical
    process. The implemented algorithms are described in
    (Dikta and Scheer (2021) <doi:10.1007/978-3-030-73480-0>)
    and can be applied
    to generalized linear models without any further implementation
    effort. As far as certain linearity conditions are fulfilled
    the resampling scheme are also applicable beyond generalized
    linear models. This is reflected in the software architecture
    which allows to reuse the resampling scheme by implementing
    only certain interfaces for models that are not supported
    natively by the package.
	"""
	
	homepage = "https://github.com/MarselScheer/bootGOF"
	cran = "bootGOF" 

	version("0.1.0", md5="bdba85fba80edf9ef226d07ffd7046c3")

	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
