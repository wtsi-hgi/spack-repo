# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanine2cdf(RPackage):
	"""canine2cdf

	A package containing an environment representing the Canine_2.cdf file.
	"""
	
	bioc = "canine2cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/canine2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/canine2cdf/canine2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="78740cde98c75e6680470564a4df74c3")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation