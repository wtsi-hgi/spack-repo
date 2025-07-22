# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDavidtiling(RPackage):
	"""Data and analysis scripts for David, Huber et al. yeast tiling array paper

	This package contains the data for the paper by L. David et al. in PNAS 2006 (PMID 16569694): 8 CEL files of Affymetrix genechips, an ExpressionSet object with the raw feature data, a probe annotation data structure for the chip and the yeast genome annotation (GFF file) that was used. In addition, some custom-written analysis functions are provided, as well as R scripts in the scripts directory.
	"""
	
	homepage = "http://www.ebi.ac.uk/huber"
	bioc = "davidTiling"

	version("1.48.0", commit="8354c0c44d1c7956d125841b53846922fbdd2684")
	version("1.42.0", commit="5d00106ec5f9aafd1df1d48b27ddee441bc3bbd0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-tilingarray", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))

