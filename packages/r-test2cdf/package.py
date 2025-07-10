# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest2cdf(RPackage):
	"""test2cdf

	A package containing an environment representing the Test2.CDF file.
	"""
	
	bioc = "test2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/test2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/test2cdf/test2cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="1c8a0874f491d4646fbc48d4793025c2ea3a09c442f216f36fe6ed0df4f12843")

	depends_on("r-annotationdbi", type=("build", "run"))

