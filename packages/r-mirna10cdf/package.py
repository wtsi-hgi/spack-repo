# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna10cdf(RPackage):
	"""mirna10cdf

	A package containing an environment representing the miRNA-1_0.CDF file.
	"""
	
	bioc = "mirna10cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirna10cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirna10cdf/mirna10cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="814da2a2e298e132f4db0b2e8ab814be")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation