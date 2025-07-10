# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna10cdf(RPackage):
	"""mirna10cdf

	A package containing an environment representing the miRNA-1_0.CDF file.
	"""
	
	bioc = "mirna10cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirna10cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirna10cdf/mirna10cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="cb43a224c3e5ae7aed471013ada7e78d8f787f1855cc242c573b1cd05b60cf90")

	depends_on("r-annotationdbi", type=("build", "run"))

