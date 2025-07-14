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

	version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="b282e7ab71e8404bd2064e0fd9c51503b01dbc2e4603931e417cc0abbb23571b")

	depends_on("r@1.4.1:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

