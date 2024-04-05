# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPumadata(RPackage):
	"""Various data sets for use with the puma package

	This is a simple data package including various data sets derived from the estrogen data for use with the puma (Propagating Uncertainty in Microarray Analysis) package.
	"""
	
	homepage = "http://umber.sbs.man.ac.uk/resources/puma"
	bioc = "pumadata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pumadata_2.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pumadata/pumadata_2.38.0.tar.gz"]

	version("2.38.0", md5="811d6234d1d4e310beb7111601b157b7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-puma", type=("build", "run"))
	depends_on("r-oligo@1.32:", type=("build", "run"))

