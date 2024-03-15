# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	version("2.10.0", md5="bea896eadb8eb999e48d1cf5974dfe9e")

	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-annotationhub@3.3.6:", type=("build", "run"))
	depends_on("r-biocfilecache@1.5.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
