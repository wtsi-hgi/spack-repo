# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133atagcdf(RPackage):
	"""hgu133atagcdf

	A package containing an environment representing the HG-U133A_tag.CDF file.
	"""
	
	bioc = "hgu133atagcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133atagcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133atagcdf/hgu133atagcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="01f8809e0deb5b83f3f0decec881a1d8")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation