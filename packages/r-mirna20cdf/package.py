# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna20cdf(RPackage):
	"""mirna20cdf

	A package containing an environment representing the miRNA-2_0.cdf file.
	"""
	
	bioc = "mirna20cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mirna20cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mirna20cdf/mirna20cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="56f7807673ff108427ae7f6bdf85ae1c")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation