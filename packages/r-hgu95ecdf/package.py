# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95ecdf(RPackage):
	"""hgu95ecdf

	A package containing an environment representing the HG_U95E.CDF file.
	"""
	
	bioc = "hgu95ecdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu95ecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu95ecdf/hgu95ecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="fa27cfff62a38fc51640d797bd628105")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation