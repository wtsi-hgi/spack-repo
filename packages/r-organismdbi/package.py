# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrganismdbi(RPackage):
	"""Software to enable the smooth interfacing of different database
	packages.

	The package enables a simple unified interface to several annotation
	packages each of which has its own schema by taking advantage of the
	fact that each of these packages implements a select methods."""

	bioc = "OrganismDbi"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OrganismDbi_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OrganismDbi/OrganismDbi_1.44.0.tar.gz"]

	version("1.44.0", md5="3d6c3ba042e4e0b6ecf5fa27fc344a82")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-annotationdbi@1.33.15:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.39.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-genomicranges@1.31.13:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
