# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowmacaannotation(RPackage):
	"""LowMACAAnnotation

	A package containing the data to run LowMACA package.
	"""
	
	bioc = "LowMACAAnnotation" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/LowMACAAnnotation_0.99.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/LowMACAAnnotation/LowMACAAnnotation_0.99.3.tar.gz"]

	version("0.99.3", md5="9e0d3fe7f30fe48aef9c4387eb5bacfa")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation