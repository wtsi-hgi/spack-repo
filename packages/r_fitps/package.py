# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitps(RPackage):
	"""Fit Zeta Distributions to Forensic Data

	Fits Zeta distributions (discrete power laws) to data that arises
    from forensic surveys of clothing on the presence of glass and paint in
    various populations. The general method is described to some extent in
    Coulson, S.A., Buckleton, J.S., Gummer, A.B., and Triggs, C.M. (2001) 
    <doi:10.1016/S1355-0306(01)71847-3>, although the implementation differs.
	"""
	
	homepage = "https://github.com/jmcurran/fitPS"
	cran = "fitPS" 

	version("1.0.1", md5="543dce0f81e933c90b5a859a674c007b")
	version("1.0.0", md5="548eab976137a864e0389a8ebf8b8a54")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
