# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndexwizard(RPackage):
	"""Constructing and Analyzing Complex Selection Indices

	Allows the construction selection indices based on estimated breeding values in animal and plant breeding and to calculate several analytic measures around to assess its impact on genetic and phenotypic progress. The methodology thereby allows to analyze genetic gain of traits in the breeding goal which are not part of the actual index and automatically computes several analytic measures. It further allows to retrospectively derive realized economic weights from observed genetic trends. The framework is described in Simianer, H., Heise, J., Rensing, S., Pook, T. Geibel, J. and Reimer, C. (2023) <doi:10.1186/s12711-023-00807-0>.
	"""
	
	homepage = "https://github.com/johannesgeibel/IndexWizard"
	cran = "IndexWizard" 

	version("0.2.1.0", md5="a6ef6fe7b3a3342c66d9f377625ff4ea")

