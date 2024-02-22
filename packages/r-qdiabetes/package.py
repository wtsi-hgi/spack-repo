# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdiabetes(RPackage):
	"""Type 2 Diabetes Risk Calculator

	Calculate the risk of developing type 2 diabetes using risk prediction algorithms derived by 'ClinRisk'.
	"""
	
	homepage = "https://github.com/Feakster/qdiabetes"
	cran = "QDiabetes" 

	version("1.0-2", md5="ecbbb71b445a2642aeeac83c02c3f435")

	depends_on("r@2.10:", type=("build", "run"))
