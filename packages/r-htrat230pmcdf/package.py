# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtrat230pmcdf(RPackage):
	"""htrat230pmcdf

	A package containing an environment representing the HT_Rat230_PM.cdf file.
	"""
	
	bioc = "htrat230pmcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htrat230pmcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htrat230pmcdf/htrat230pmcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="c6683d16e8aacccd326f7a7eebb79b98")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation