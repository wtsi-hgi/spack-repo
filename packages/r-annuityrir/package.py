# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnuityrir(RPackage):
	"""Annuity Random Interest Rates

	Annuity Random Interest Rates proposes different techniques for the approximation of the present and final value of a unitary annuity-due or annuity-immediate considering interest rate as a random variable. Cruz Rambaud et al. (2017) <doi:10.1007/978-3-319-54819-7_16>. Cruz Rambaud et al. (2015) <doi:10.23755/rm.v28i1.25>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "AnnuityRIR" 

	version("1.0-0", md5="4d35f503a422974d126f35fac685f912")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
