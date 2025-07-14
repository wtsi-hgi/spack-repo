# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimutacionsdata(RPackage):
	"""Data for epimutacions package

	This package includes the data necessary to run functions and examples in epimutacions package. Collection of DNA methylation data. The package contains 2 datasets: (1) Control ( GEO: GSE104812), (GEO: GSE97362) case samples; and (2) reference panel (GEO: GSE127824). It also contains candidate regions to be epimutations in 450k methylation arrays.
	"""
	
	homepage = "https://github.com/LeireAbarrategui/epimutacionsData"
	bioc = "epimutacionsData"

	version("1.12.0", commit="c7a24c473a8cb006355daac7462160d4cd257580")
	version("1.6.0", commit="9f31975df07ee17f91e87b8cd52bbaff4393c3b3")

	depends_on("r@4.2:", type=("build", "run"))

