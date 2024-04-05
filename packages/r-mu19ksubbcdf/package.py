# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubbcdf(RPackage):
	"""mu19ksubbcdf

	A package containing an environment representing the Mu19KsubB.CDF file.
	"""
	
	bioc = "mu19ksubbcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu19ksubbcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu19ksubbcdf/mu19ksubbcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="35e5ebcb4cb51950a85c1e3622bb39f0")

	depends_on("r-annotationdbi", type=("build", "run"))

