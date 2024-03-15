# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlaevis2cdf(RPackage):
	"""xlaevis2cdf

	A package containing an environment representing the X_laevis_2.CDF file.
	"""
	
	bioc = "xlaevis2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xlaevis2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xlaevis2cdf/xlaevis2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9e4a80d66397299b4e66a8d6715ca4aa")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation