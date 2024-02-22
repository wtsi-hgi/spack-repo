# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhsPredict(RPackage):
	"""Breast Cancer Survival and Therapy Benefits

	Calculate Overall Survival or Recurrence-Free Survival for breast cancer patients, using 'NHS Predict'. 
            The time interval for the estimation can be set up to 15 years, with default at 10.
            Incremental therapy benefits are estimated for hormone therapy, chemotherapy, trastuzumab, and bisphosphonates.
            An additional function, suited for SCAN audits, features a more user-friendly version of the code, with fewer inputs, but necessitates
            the correct standardised inputs.
            This work is not affiliated with the development of 'NHS Predict' and its underlying statistical model.
            Details on 'NHS Predict' can be found at: <doi:10.1186/bcr2464>.
            The web version of 'NHS Predict': <https://breast.predict.nhs.uk/>.
            A small dataset of 50 fictional patient observations is provided for the purpose of running examples with the main two functions,
            and an additional dataset is provided for running example with the dedicated SCAN function.
	"""
	
	cran = "nhs.predict" 

	version("1.4.0", md5="c17203fb6807fd949ad187f2fe1c451a")

	depends_on("r@3.5:", type=("build", "run"))
