# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosophila2cdf(RPackage):
	"""drosophila2cdf

	A package containing an environment representing the Drosophila_2.cdf file.
	"""
	
	bioc = "drosophila2cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/drosophila2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/drosophila2cdf/drosophila2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="3323e723c133ff2b6188e22bebf3e20a")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation