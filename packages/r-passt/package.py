# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasst(RPackage):
	"""Probability Associator Time (PASS-T)

	Simulates judgments of frequency and duration based on
    the Probability Associator Time (PASS-T) model. PASS-T is a memory
    model based on a simple competitive artificial neural network. It 
    can imitate human judgments of frequency and duration, which have
    been extensively studied in cognitive psychology
    (e.g. Hintzman (1970) <doi:10.1037/h0028865>, Betsch et al. (2010)
    <https://psycnet.apa.org/record/2010-18204-003>). The PASS-T model
    is an extension of the PASS model (Sedlmeier, 2002,
    ISBN:0198508638). The package provides an easy way to run
    simulations, which can then be compared with empirical data in
    human judgments of frequency and duration.
	"""
	
	homepage = "https://github.com/johannes-titz/passt"
	cran = "passt" 

	version("0.1.3", md5="2c44339769cfc70ecf0e7cd473dda561")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
