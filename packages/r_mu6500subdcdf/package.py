# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu6500subdcdf(RPackage):
	"""mu6500subdcdf

	A package containing an environment representing the Mu6500subD.CDF file.
	"""
	
	bioc = "mu6500subdcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu6500subdcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu6500subdcdf/mu6500subdcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="a614674e8bc60fefd8520dd25d45f8d0")

	depends_on("r-annotationdbi", type=("build", "run"))

