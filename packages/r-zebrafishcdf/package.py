# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishcdf(RPackage):
	"""zebrafishcdf

	A package containing an environment representing the Zebrafish.cdf file.
	"""
	
	bioc = "zebrafishcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafishcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/zebrafishcdf/zebrafishcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="04edbb632600c97610b86423c2d850e7")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation