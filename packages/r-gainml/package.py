# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGainml(RPackage):
	"""Machine Learning-Based Analysis of Potential Power Gain from
Passive Device Installation on Wind Turbine Generators

	Provides an effective machine learning-based tool that quantifies the gain of passive device installation on wind turbine generators.
  H. Hwangbo, Y. Ding, and D. Cabezon (2019) <arXiv:1906.05776>.
	"""
	
	cran = "gainML" 

	version("0.1.0", md5="a50668365c47f40f75bb73a06f5cee8e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fields@9:", type=("build", "run"))
	depends_on("r-fnn@1.1:", type=("build", "run"))
