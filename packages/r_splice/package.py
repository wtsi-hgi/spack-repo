# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplice(RPackage):
	"""Synthetic Paid Loss and Incurred Cost Experience (SPLICE)
Simulator

	An extension to the individual claim simulator called 'SynthETIC'
    (on CRAN), to simulate the evolution of case estimates of incurred losses
    through the lifetime of an insurance claim. The transactional simulation
    output now comprises key dates, and both claim payments and revisions of
    estimated incurred losses. An initial set of test parameters, designed to
    mirror the experience of a real insurance portfolio, were set up and applied
    by default to generate a realistic test data set of incurred histories (see
    vignette). However, the distributional assumptions used to generate this
    data set can be easily modified by users to match their experiences.
    Reference: Avanzi B, Taylor G, Wang M (2021) "SPLICE: A Synthetic Paid Loss
    and Incurred Cost Experience Simulator" <arXiv:2109.04058>.
	"""
	
	homepage = "https://github.com/agi-lab/SPLICE"
	cran = "SPLICE" 

	version("1.1.2", md5="2a1108f95eed3be1831975569108ebe0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-synthetic@1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
