# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu6500subbcdf(RPackage):
	"""mu6500subbcdf

	A package containing an environment representing the Mu6500subB.CDF file.
	"""
	
	bioc = "mu6500subbcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu6500subbcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu6500subbcdf/mu6500subbcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="5000bea2a018b4b6ec05cda111438bc1")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation