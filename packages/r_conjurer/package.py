# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConjurer(RPackage):
	"""A Parametric Method for Generating Synthetic Data

	Generates synthetic data distributions to enable testing various modelling techniques in ways that real data does not allow. Noise can be added in a controlled manner such that the data seems real. This methodology is generic and therefore benefits both the academic and industrial research.
	"""
	
	homepage = "https://www.foyi.co.nz/posts/documentation/documentationconjurer/"
	cran = "conjurer" 

	version("1.7.1", md5="5a0ca8ed4500ad13e2da161d7f1bd690")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
