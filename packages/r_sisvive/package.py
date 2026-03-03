# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSisvive(RPackage):
	"""Some Invalid Some Valid Instrumental Variables Estimator

	Selects invalid instruments amongst a candidate of potentially bad instruments. The algorithm selects potentially invalid instruments and provides an estimate of the causal effect between exposure and outcome.
	"""
	
	cran = "sisVIVE" 

	version("1.4", md5="75830c23970fff8a43a02f532d03a89d")

	depends_on("r-lars", type=("build", "run"))
