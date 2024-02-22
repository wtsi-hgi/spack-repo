# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPleio(RPackage):
	"""Pleiotropy Test for Multiple Traits on a Genetic Marker

	Perform tests for pleiotropy of multiple traits of various variable types on genotypes for a genetic marker.
	"""
	
	homepage = "https://bioinformaticstools.mayo.edu/research/pleio/"
	cran = "pleio" 

	version("1.9", md5="f8b470ad3b16c62136b29b5811d00199")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
