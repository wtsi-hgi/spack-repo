# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHivprtplus2cdf(RPackage):
	"""hivprtplus2cdf

	A package containing an environment representing the HIV PRTPlus 2.CDF file.
	"""
	
	bioc = "hivprtplus2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hivprtplus2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hivprtplus2cdf/hivprtplus2cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="c4bd585bfbfce339d27550ce2718c9a943e3e0b19f1f8437e9e7cf28d5c764cb")

	depends_on("r-annotationdbi", type=("build", "run"))

