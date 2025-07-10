# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgcdf(RPackage):
	"""agcdf

	A package containing an environment representing the AG.CDF file.
	"""
	
	bioc = "agcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/agcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/agcdf/agcdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="f22ce37f7982e2f2bfbacccf59067d8bf4b407fde7a2c9b4f0fe68cc5b20181e")

	depends_on("r-annotationdbi", type=("build", "run"))

