# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsMm9(RPackage):
	"""RnBeads.mm9

	Automatically generated RnBeads annotation package for the assembly mm9.
	"""
	
	bioc = "RnBeads.mm9" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.mm9_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.mm9/RnBeads.mm9_1.34.0.tar.gz"]

	version("1.34.0", md5="76f271051b1c542e5ac0da492777f933", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.mm9_1.34.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

	# experiment