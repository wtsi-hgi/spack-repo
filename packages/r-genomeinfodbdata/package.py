# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomeinfodbdata(RPackage):
	"""for mapping between NCBI taxonomy ID and species. Used by functions
	in the GenomeInfoDb package."""

	bioc = "GenomeInfoDbData"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/GenomeInfoDbData_1.2.11.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/GenomeInfoDbData/GenomeInfoDbData_1.2.11.tar.gz"]

	version("1.2.11", md5="2a4cbfc2031992fed3c9445f450890a2")

	depends_on("r@3.5:", type=("build", "run"))

	# annotation