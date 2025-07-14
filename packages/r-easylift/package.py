# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasylift(RPackage):
	"""An R package to perform genomic liftover

	The easylift package provides a convenient tool for genomic liftover operations between different genome assemblies. It seamlessly works with Bioconductor's GRanges objects and chain files from the UCSC Genome Browser, allowing for straightforward handling of genomic ranges across various genome versions. One noteworthy feature of easylift is its integration with the BiocFileCache package. This integration automates the management and caching of chain files necessary for liftover operations. Users no longer need to manually specify chain file paths in their function calls, reducing the complexity of the liftover process.
	"""
	
	homepage = "https://github.com/nahid18/easylift"
	bioc = "easylift"

	version("1.6.0", commit="ea18a53d44a9c4828cdf2fd14c7a3a81c478bc9f")
	version("1.0.0", commit="189965ac77e47a2d32b79265890559d582726397")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
