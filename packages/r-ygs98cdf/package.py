# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYgs98cdf(RPackage):
	"""ygs98cdf

	A package containing an environment representing the YG_S98.cdf file.
	"""
	
	bioc = "ygs98cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ygs98cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ygs98cdf/ygs98cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="b00a1ca4dc02ef3b72bf080ed79b0f580e98d307b735af541854d405555c0448")

	depends_on("r-annotationdbi", type=("build", "run"))

