# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamsignals(RPackage):
	"""Extract read count signals from bam files.

	This package allows to efficiently obtain count vectors from indexed bam
	files. It counts the number of reads in given genomic ranges and it
	computes reads profiles and coverage profiles. It also handles paired-
	end data."""

	bioc = "bamsignals"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bamsignals_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bamsignals/bamsignals_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.8.0", commit="b123b83e8e026c9ec91209d4498aff3e95a5de23")
	version("1.34.0", sha256="6478d16da52f29e5f790f3f39c04c3f0b278fb47b5bfdce09a992b649b7f62e3")
	version("1.32.0", commit="34bfc4e8b58e47c3b94347fd2976aeae07fc28c2")
	version("1.30.0", commit="aac37dffd6f6876b4626866e3d40bb7af75620fe")
	version("1.28.0", commit="27b70be6f73747d9d32054da043f4a37ea55b917")
	version("1.26.0", commit="d57643441d04f77db0907637dc9e7cd5bed5842f")
	version("1.22.0", commit="5f533969c84212406bcb3ebf725ebb6d77e9947a")
	version("1.16.0", commit="dba9a4ae1613d2700f122ade1e9b90ca8fce5657")
	version("1.14.0", commit="3107d3a35830e879eeddf127a81016ea1ca9b53d")
	version("1.12.1", commit="06b6282df377cf9db58e8016be4ac8ddcc960939")
	version("1.10.0", commit="7499312ce71e8680680eda10b49d7dff682fc776")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("lzma", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
