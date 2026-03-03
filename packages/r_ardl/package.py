# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArdl(RPackage):
	"""ARDL, ECM and Bounds-Test for Cointegration

	Creates complex autoregressive distributed lag (ARDL) models and 
    constructs the underlying unrestricted and restricted error correction 
    model (ECM) automatically, just by providing the order. It also performs
    the bounds-test for cointegration as described in Pesaran et al. (2001) 
    <doi:10.1002/jae.616> and provides the multipliers and the cointegrating
    equation. The validity and the accuracy of this package have been verified 
    by successfully replicating the results of Pesaran et al. (2001) in 
    Natsiopoulos and Tzeremes (2022) <doi:10.1002/jae.2919>.
	"""
	
	homepage = "https://github.com/Natsiopoulos/ARDL"
	cran = "ARDL" 

	version("0.2.4", md5="ce1246aa9fccc207bafb8f432722c036")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynlm", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
