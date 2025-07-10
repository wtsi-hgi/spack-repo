# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNadfinder(RPackage):
	"""Call wide peaks for sequencing data

	Nucleolus is an important structure inside the nucleus in eukaryotic cells. It is the site for transcribing rDNA into rRNA and for assembling ribosomes, aka ribosome biogenesis. In addition, nucleoli are dynamic hubs through which numerous proteins shuttle and contact specific non-rDNA genomic loci. Deep sequencing analyses of DNA associated with isolated nucleoli (NAD- seq) have shown that specific loci, termed nucleolus- associated domains (NADs) form frequent three- dimensional associations with nucleoli. NAD-seq has been used to study the biological functions of NAD and the dynamics of NAD distribution during embryonic stem cell (ESC) differentiation. Here, we developed a Bioconductor package NADfinder for bioinformatic analysis of the NAD-seq data, including baseline correction, smoothing, normalization, peak calling, and annotation.
	"""
	
	bioc = "NADfinder" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NADfinder_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NADfinder/NADfinder_1.26.0.tar.gz"]

	version("1.26.0", sha256="b8f71e6e168bc500b9d8af3a49b0183edb6f04904b8dd6e5036b70ce0c3ee2c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-trackviewer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-empiricalbrownsmethod", type=("build", "run"))
	depends_on("r-atacseqqc", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-csaw", type=("build", "run"))
