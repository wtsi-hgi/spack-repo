# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyebiasexamples(RPackage):
	"""Example data for the dyebias package, which implements the GASSCO method.

	Data for the dyebias package, consisting of 4 self-self hybrizations of self-spotted yeast slides, as well as data from Array Express accession E-MTAB-32
	"""
	
	homepage = "http://www.holstegelab.nl/publications/margaritis_lijnzaad"
	bioc = "dyebiasexamples" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/dyebiasexamples_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/dyebiasexamples/dyebiasexamples_1.42.0.tar.gz"]

	version("1.42.0", md5="b73aa6c0c98150b2bccba7802dda8c86")

	depends_on("r@1.4.1:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

	# experiment