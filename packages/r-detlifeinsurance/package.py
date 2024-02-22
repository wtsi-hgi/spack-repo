# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetlifeinsurance(RPackage):
	"""Life Insurance Premium and Reserves Valuation

	Methods for valuation of life insurance premiums and reserves (including variable-benefit and fractional coverage) based on  "Actuarial Mathematics" by Bowers, H.U. Gerber, J.C. Hickman, D.A. Jones and C.J. Nesbitt (1997, ISBN: 978-0938959465), "Actuarial Mathematics for Life Contingent Risks" by Dickson, David C. M., Hardy, Mary R. and Waters, Howard R  (2009) <doi:10.1017/CBO9780511800146>  and "Life Contingencies" by Jordan, C. W (1952) <doi:10.1017/S002026810005410X>. It also contains functions for  equivalent interest and discount rate calculation, present and future values of annuities, and loan amortization schedule.
	"""
	
	homepage = "https://github.com/JoaquinAuza/DetLifeInsurance"
	cran = "DetLifeInsurance" 

	version("0.1.3", md5="b273e58c14dd8391360ec1125272ad23")

	depends_on("r@3.5:", type=("build", "run"))
