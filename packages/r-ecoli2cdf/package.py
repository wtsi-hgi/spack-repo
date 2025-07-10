# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoli2cdf(RPackage):
	"""ecoli2cdf

	A package containing an environment representing the E_coli_2.cdf file.
	"""
	
	bioc = "ecoli2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoli2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoli2cdf/ecoli2cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="39a9dd100a53ec47a8b6dab0714b9f742dc25e36efa65f90496f26dc14cf7de6")

	depends_on("r-annotationdbi", type=("build", "run"))

