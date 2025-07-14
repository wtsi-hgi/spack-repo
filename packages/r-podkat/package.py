# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPodkat(RPackage):
	"""Position-Dependent Kernel Association Test

	This package provides an association test that is capable of dealing with very rare and even private variants. This is accomplished by a kernel-based approach that takes the positions of the variants into account. The test can be used for pre-processed matrix data, but also directly for variant data stored in VCF files. Association testing can be performed whole-genome, whole-exome, or restricted to pre-defined regions of interest. The test is complemented by tools for analyzing and visualizing the results.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/podkat/"
	bioc = "podkat" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/podkat_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/podkat/podkat_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="28392b4e431fafeb56fd006e067c8ae45073f0627697a51dddd973b8ce100300")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsamtools@1.99.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome@1.32:", type=("build", "run"))
	depends_on("r-rhtslib@1.15.3:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
