# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssa(RPackage):
	"""Applied Singular Spectrum Analysis (ASSA)

	Functions to model and decompose time series into principal components using singular spectrum analysis (de Carvalho and Rua (2017) <doi:10.1016/j.ijforecast.2015.09.004>; de Carvalho et al (2012) <doi:10.1016/j.econlet.2011.09.007>).
	"""
	
	cran = "ASSA" 

	version("2.0", md5="28c91e058c2274ad450bf6ace32fbf27")

	depends_on("r@3.6:", type=("build", "run"))
