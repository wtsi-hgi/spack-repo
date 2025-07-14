# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCexor(RPackage):
	"""An R package to uncover high-resolution protein-DNA interactions in ChIP-exo replicates

	Strand specific peak-pair calling in ChIP-exo replicates. The cumulative Skellam distribution function is used to detect significant normalised count differences of opposed sign at each DNA strand (peak-pairs). Then, irreproducible discovery rate for overlapping peak-pairs across biological replicates is computed.
	"""
	
	bioc = "CexoR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CexoR_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CexoR/CexoR_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="c464cda22f9c2d96a0069ce77498162ccf83bc75dda7360b45c0ccfaea26cb65")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-idr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-genomation", type=("build", "run"))
