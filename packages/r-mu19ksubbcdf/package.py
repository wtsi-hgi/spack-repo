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

	version("2.18.0", sha256="644208a5656546e84595414667c20620be249e0ff4081e16f2e4d82696fa51f1")

	depends_on("r-annotationdbi", type=("build", "run"))

