# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230bcdf(RPackage):
	"""rae230bcdf

	A package containing an environment representing the RAE230B.CDF file.
	"""
	
	bioc = "rae230bcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rae230bcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rae230bcdf/rae230bcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="bd61c17402e9c04be1000c16e0356618")

	depends_on("r-annotationdbi", type=("build", "run"))

