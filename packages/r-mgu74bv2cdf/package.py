# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74bv2cdf(RPackage):
	"""mgu74bv2cdf

	A package containing an environment representing the MG_U74Bv2.CDF file.
	"""
	
	bioc = "mgu74bv2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74bv2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74bv2cdf/mgu74bv2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="45c48d11af03633dc10f8682b7ad74c5")

	depends_on("r-annotationdbi", type=("build", "run"))

