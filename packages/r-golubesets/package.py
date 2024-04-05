# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGolubesets(RPackage):
	"""exprSets for golub leukemia data

	representation of public golub data with some covariate data of provenance unknown to the maintainer at present; now employs ExpressionSet format
	"""
	
	bioc = "golubEsets" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/golubEsets_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/golubEsets/golubEsets_1.44.0.tar.gz"]

	version("1.44.0", md5="49e3527c00f06c189a048a6b871f3d54")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

