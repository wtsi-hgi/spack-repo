# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcsubset(RPackage):
	"""Experimental Data Package: MAQCsubset

	Data Package automatically created on Sun Nov 19 15:59:29 2006.
	"""
	
	bioc = "MAQCsubset" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MAQCsubset_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MAQCsubset/MAQCsubset_1.40.0.tar.gz"]

	version("1.40.0", sha256="6490ed55e3cf216d8e90ac29506d1292880aca53ffda6091b0b365295c2516e3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

