# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubdcdf(RPackage):
	"""hu35ksubdcdf

	A package containing an environment representing the Hu35KsubD.CDF file.
	"""
	
	bioc = "hu35ksubdcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hu35ksubdcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hu35ksubdcdf/hu35ksubdcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="6f6423426969f306fb0d5171e75b5380")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation