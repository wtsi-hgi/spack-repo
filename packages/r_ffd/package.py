# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfd(RPackage):
	"""Freedom from Disease

	Functions, S4 classes/methods and a graphical user interface (GUI) to design surveys to substantiate freedom from disease using a modified hypergeometric function (see Cameron and Baldock, 1997, <doi:10.1016/s0167-5877(97)00081-0>). Herd sensitivities are computed according to sampling strategies "individual sampling" or "limited sampling" (see M. Ziller, T. Selhorst, J. Teuffert, M. Kramer and H. Schlueter, 2002, <doi:10.1016/S0167-5877(01)00245-8>). Methods to compute the a-posteriori alpha-error are implemented. Risk-based targeted sampling is supported.
	"""
	
	homepage = "http://ffd.r-forge.r-project.org"
	cran = "FFD" 

	version("1.0-9", md5="d156a777b2b7bec785f0f7a6c13ce8a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
