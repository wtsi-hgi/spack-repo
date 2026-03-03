# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuerelativerisk(RPackage):
	"""Relative Risk Based on the Ratio of Median Unbiased Estimates

	Implements an estimator for relative risk based on the median unbiased estimator. The relative risk estimator is well defined and performs satisfactorily for a wide range of data configurations. The details of the method are available in Carter et al (2010) <doi:10.1111/j.1467-9876.2010.00711.x>.
	"""
	
	cran = "mueRelativeRisk" 

	version("0.1.1", md5="df47da24b240894a57f9431be81a7cc2")

	depends_on("r@3.2.3:", type=("build", "run"))
