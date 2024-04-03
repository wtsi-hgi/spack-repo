# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimenthub(RPackage):
	"""Client to access ExperimentHub resources.

	This package provides a client for the Bioconductor ExperimentHub web
	resource. ExperimentHub provides a central location where curated data from
	experiments, publications or training courses can be accessed. Each
	resource has associated metadata, tags and date of modification. The client
	creates and manages a local cache of files retrieved enabling quick and
	reproducible access."""

	bioc = "ExperimentHub"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ExperimentHub_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ExperimentHub/ExperimentHub_2.10.0.tar.gz"]
	version("2.8.0", commit="f25c854c51878844098290a05936cb35b235f30e")
	version("2.6.0", commit="557ba29720bce85902a85445dd0435b7356cdd7f")
	version("2.4.0", commit="bdce35d3a89e8633cc395f28991e6b5d1eccbe8e")
	version("2.2.1", commit="4e10686fa72baefef5d2990f41a7c44c527a7a7d")
	version("1.16.1", commit="61d51b7ca968d6cc1befe299e0784d9a19ca51f6")
	version("2.10.0", md5="bea896eadb8eb999e48d1cf5974dfe9e")

	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-annotationhub@3.3.6:", type=("build", "run"))
	depends_on("r-biocfilecache@1.5.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
