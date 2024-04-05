# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74av2cdf(RPackage):
	"""mgu74av2cdf

	A package containing an environment representing the MG_U74Av2.CDF file.
	"""
	
	bioc = "mgu74av2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74av2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74av2cdf/mgu74av2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="35e2abb9fbfd68d90dc32a2faae00c95")

	depends_on("r-annotationdbi", type=("build", "run"))

