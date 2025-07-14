# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaryoploter(RPackage):
	"""Plot customizable linear genomes displaying arbitrary data

	karyoploteR creates karyotype plots of arbitrary genomes and offers a complete set of functions to plot arbitrary data on them. It mimicks many R base graphics functions coupling them with a coordinate change function automatically mapping the chromosome and data coordinates into the plot coordinates. In addition to the provided data plotting functions, it is easy to add new ones.
	"""
	
	homepage = "https://github.com/bernatgel/karyoploteR"
	bioc = "karyoploteR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/karyoploteR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/karyoploteR/karyoploteR_1.28.0.tar.gz"]

    version("1.34.2", tag="RELEASE_3_21")
	version("1.28.0", sha256="4118fadaba72b8493da7f38369b347ad416f98597d0302a131206950c4a5294b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-bezier", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-bamsignals", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
