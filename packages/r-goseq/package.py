# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoseq(RPackage):
	"""Gene Ontology analyser for RNA-seq and other length biased data.

	Detects Gene Ontology and/or other user defined categories which are
	over/under represented in RNA-seq data"""

	bioc = "goseq"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/goseq_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/goseq/goseq_1.54.0.tar.gz"]

	version("1.54.0", md5="4c39d7fbb51594a70dd3e54b1bc10375")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-genelendatabase@1.9.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
