# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesizeestimator(RPackage):
	"""Calculate Sample Size for Various Scenarios

	Calculates sample size for various scenarios, such as sample size
    to estimate population proportion with stated absolute or relative
    precision, testing a single proportion with a reference value, to estimate
    the population mean with stated absolute or relative precision, testing
    single mean with a reference value and sample size for comparing two
    unpaired or independent means, comparing two paired means, the sample size
    For case control studies, estimating the odds ratio with stated precision,
    testing the odds ratio with a reference value, estimating relative risk with
    stated precision, testing relative risk with a reference value, testing
    a correlation coefficient with a specified value, etc. 
    <https://www.academia.edu/39511442/Adequacy_of_Sample_Size_in_Health_Studies#:~:text=Determining%20the%20sample%20size%20for,may%20yield%20statistically%20inconclusive%20results.>. 
	"""
	
	cran = "samplesizeestimator" 

	version("1.0.0", md5="e4a5e728c08308f92091a9d80e0f579d")

	depends_on("r-stringi", type=("build", "run"))
