# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430pmcdf(RPackage):
	"""htmg430pmcdf

	A package containing an environment representing the HT_MG-430_PM.cdf file.
	"""
	
	bioc = "htmg430pmcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/htmg430pmcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/htmg430pmcdf/htmg430pmcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="016a54b47adbbed7db989787646a0084")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation