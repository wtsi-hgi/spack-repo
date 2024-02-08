# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationhub(RPackage):
	"""Client to access AnnotationHub resources.

	This package provides a client for the Bioconductor AnnotationHub web
	resource. The AnnotationHub web resource provides a central location
	where genomic files (e.g., VCF, bed, wig) and other resources from
	standard locations (e.g., UCSC, Ensembl) can be discovered. The resource
	includes metadata about each resource, e.g., a textual description,
	tags, and date of modification. The client creates and manages a local
	cache of files retrieved by the user, helping with quick and
	reproducible access."""

	bioc = "AnnotationHub"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AnnotationHub_3.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AnnotationHub/AnnotationHub_3.10.0.tar.gz"]

	version("3.10.0", md5="9dcc8ea705c0e7f8ac8e9af262de876f")

	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-biocfilecache@1.5.1:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biocversion", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-annotationdbi@1.31.19:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-interactivedisplaybase", type=("build", "run"))
