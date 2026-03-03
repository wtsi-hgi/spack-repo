# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMecor(RPackage):
	"""Measurement Error Correction in Linear Models with a Continuous
Outcome

	Covariate measurement error correction is implemented by means of regression calibration by Carroll RJ, Ruppert D, Stefanski LA & Crainiceanu CM (2006, ISBN:1584886331), efficient regression calibration by Spiegelman D, Carroll RJ & Kipnis V (2001) <doi:10.1002/1097-0258(20010115)20:1%3C139::AID-SIM644%3E3.0.CO;2-K> and maximum likelihood estimation by Bartlett JW, Stavola DBL & Frost C (2009) <doi:10.1002/sim.3713>. Outcome measurement error correction is implemented by means of the method of moments by Buonaccorsi JP (2010, ISBN:1420066560) and efficient method of moments by Keogh RH, Carroll RJ, Tooze JA, Kirkpatrick SI & Freedman LS (2014) <doi:10.1002/sim.7011>. Standard error estimation of the corrected estimators is implemented by means of the Delta method by Rosner B, Spiegelman D & Willett WC (1990) <doi:10.1093/oxfordjournals.aje.a115715> and Rosner B, Spiegelman D & Willett WC (1992) <doi:10.1093/oxfordjournals.aje.a116453>, the Fieller method described by Buonaccorsi JP (2010, ISBN:1420066560), and the Bootstrap by Carroll RJ, Ruppert D, Stefanski LA & Crainiceanu CM (2006, ISBN:1584886331).
	"""
	
	homepage = "https://github.com/LindaNab/mecor"
	cran = "mecor" 

	version("1.0.0", md5="da1e8a607f48dc1ac629dca7640fe396")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
