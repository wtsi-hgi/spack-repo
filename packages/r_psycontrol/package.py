# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsycontrol(RPackage):
	"""CUSUM Person Fit Statistics

	Person fit statistics based on Quality Control measures are provided for questionnaires and tests given a specified IRT model. Statistics based on Cumulative Sum (CUSUM) charts are provided. Options are given for banks with polytomous and dichotomous data.
	"""
	
	cran = "PsyControl" 

	version("1.0.0.0", md5="d29649e0e9136935a44b3f08fb34caa3")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-irtoys", type=("build", "run"))
