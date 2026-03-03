# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2pmml(RPackage):
	"""Convert R Models to PMML

	R wrapper for the JPMML-R library <https://github.com/jpmml/jpmml-r>,
    which converts R models to Predictive Model Markup Language (PMML).
	"""
	
	homepage = "https://github.com/jpmml/r2pmml"
	cran = "r2pmml" 

	version("0.27.1", md5="2a33c2497e83932bacab4ff285fac225")

	depends_on("openjdk@1.8:", type=("build", "link", "run"))
