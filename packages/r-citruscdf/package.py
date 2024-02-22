# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitruscdf(RPackage):
	"""citruscdf

	A package containing an environment representing the Citrus.cdf file.
	"""
	
	bioc = "citruscdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/citruscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/citruscdf/citruscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="4af821a0c1ae1adf42b7dc5ce7458593")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation