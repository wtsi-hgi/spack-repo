# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdc(RPackage):
	"""Calculate Antecedent Discharge Conditions

	Calculates some antecedent discharge conditions useful in
    water quality modeling. Includes methods for calculating flow
    anomalies, base flow, and smooth discounted flows from daily flow
    measurements. Antecedent discharge algorithms are described and
    reviewed in Zhang and Ball (2017) <doi:10.1016/j.jhydrol.2016.12.052>.
	"""
	
	homepage = "https://github.com/TxWRI/adc"
	cran = "adc" 

	version("1.0.0", md5="95483c3bd55b002689175590e358551a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-runner", type=("build", "run"))
