# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrinsickappa(RPackage):
	"""Sample Size Planning Based on Intrinsic Kappa Value

	Kappa statistics is one of the most used methods to evaluate the effectiveness of inpsections based on attribute assessments in industry. However, its estimation by available methods does not provide its "real" or "intrinstic" value. This package provides functions for the computation of the intrinsic kappa value as it is described in: Rafael Sanchez-Marquez, Frank Gerhorst and David Schindler (2023) "Effectiveness of quality inspections of attributive characteristics – A novel and practical method for estimating the “intrinsic” value of kappa based on alpha and beta statistics." <doi:10.1016/j.cie.2023.109006>.
	"""
	
	cran = "intrinsicKappa" 

	version("0.1", md5="ec005bcb9b8b1b57eadcf265c45d1fcd")

	depends_on("r@4.2:", type=("build", "run"))
