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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/epimutacionsData_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/epimutacionsData/epimutacionsData_1.6.0.tar.gz"]

	version("1.6.0", sha256="d013481954019fd8d7e089af8a9f08783b45fba285e75d6df6b5e1099a0a70bd")

	depends_on("r@4.2:", type=("build", "run"))

